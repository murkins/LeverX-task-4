from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from django.contrib.auth.models import User

# importing serializers
from classroomApp import serializers

# importing models
from classroomApp.license import IsOwnerProfileOrReadOnly
from classroomApp.models import *
from django.contrib.auth.models import User


class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class PersonaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
    #permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class AllStudentsList(generics.ListAPIView):
    queryset = Persona.objects.filter(is_teacher=False)
    serializer_class = serializers.PersonaSerializer


class AllTeachersList(generics.ListAPIView):
    queryset = Persona.objects.filter(is_teacher=True)
    serializer_class = serializers.PersonaSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.filter(is_teacher=False)
    serializer_class = serializers.PersonaSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.filter(is_teacher=True)
    serializer_class = serializers.PersonaSerializer


class AllCoursesListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    # owner = Persona.objects.filter(is_teacher=True)


class AllCourseStudentsListView(generics.ListCreateAPIView):
    queryset = CourseStudent.objects.all()
    serializer_class = serializers.CourseStudentSerializer


class CourseStudentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseStudent.objects.all()
    serializer_class = serializers.CourseStudentSerializer


class AllCourseTeachersListView(generics.ListCreateAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = serializers.CourseTeacherSerializer


class CourseTeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = serializers.CourseTeacherSerializer


class LecturesListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = serializers.LectureSerializer


class LecturesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = serializers.LectureSerializer


class CourseLecturesView(generics.ListAPIView):
    serializer_class = serializers.LectureSerializer
    model = Lecture

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Lecture.objects.filter(course_id=pk)


class StudentCourseList(generics.ListAPIView):
    serializer_class = serializers.PersonaCourseSerializer
    model = CourseStudent

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CourseStudent.objects.filter(persona_id=pk).filter(persona__is_teacher=False)


class TeacherCourseList(generics.ListAPIView):
    serializer_class = serializers.PersonaCourseSerializer
    model = CourseTeacher

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CourseTeacher.objects.filter(persona_id=pk).filter(persona__is_teacher=True)


class HomeworkListView(generics.ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer


class HomeworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer


class StudentHomeworkListView(generics.ListAPIView):
    serializer_class = serializers.HomeworkSerializer
    model = Homework

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Homework.objects.filter(student_user_id=pk).filter(student_user__is_teacher=False)


class StudentLectureHomeworksListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.HomeworkSerializer
    model = Homework

    def get_queryset(self):
        pk_student = self.kwargs['pk_student']
        pk_lecture = self.kwargs['pk_lecture']

        return Homework.objects \
            .filter(student_user_id=pk_student) \
            .filter(lecture_id=pk_lecture) \
            .filter(student_user__is_teacher=False)


class MarkListCreateView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class MarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
