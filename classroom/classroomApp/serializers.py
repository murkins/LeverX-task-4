from rest_framework import serializers
from classroomApp.models import *


class PersonaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Persona
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course.name", read_only=True)
    homeworks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Lecture
        fields = ['id', 'course_name', 'course', 'title', 'present_file_name', 'hometask', 'homeworks']


class HomeworkSerializer(serializers.ModelSerializer):
    rel_mark = serializers.StringRelatedField(many=False, read_only=True)
    lecture_title = serializers.CharField(source="lecture.title", read_only=True)

    class Meta:
        model = Homework
        fields = ['solution_link', 'student_user', 'lecture', 'lecture_title', 'rel_mark']


class CourseSerializer(serializers.ModelSerializer):
    course_students = serializers.StringRelatedField(many=True, read_only=True)
    course_teachers = serializers.StringRelatedField(many=True, read_only=True)
    course_lectures = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'course_students', 'course_teachers', 'course_lectures']


class CourseStudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="persona.name", read_only=True)
    course_name = serializers.CharField(source="course.name", read_only=True)

    class Meta:
        model = CourseStudent
        fields = ['persona', 'course', 'student_name', 'course_name']


class PersonaCourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course.name", read_only=True)

    class Meta:
        model = CourseStudent
        fields = ['course_name']


class CourseTeacherSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="persona.name", read_only=True)
    course_name = serializers.CharField(source="course.name", read_only=True)

    class Meta:
        model = CourseTeacher
        fields = ['persona', 'course', 'teacher_name', 'course_name']


class MarkSerializer(serializers.ModelSerializer):
    lecture_name = serializers.CharField(source="lecture.title", read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Mark
        fields = ['lecture_name', 'homework', 'value', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'body', 'date', 'mark']
