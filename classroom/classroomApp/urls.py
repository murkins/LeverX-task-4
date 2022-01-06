"""classroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from classroomApp import views

from .views import PersonaListCreateView, PersonaDetailView

urlpatterns = [
    path("personas/", PersonaListCreateView.as_view(), name="personas"),
    path("personas/<int:pk>/", PersonaDetailView.as_view(), name="persona"),

    path("students/", views.AllStudentsList.as_view()),
    path("teachers/", views.AllTeachersList.as_view()),

    path("courses/", views.AllCoursesListCreateView.as_view()),
    path("courses/<int:pk>/", views.CourseDetailView.as_view()),
    path("courses/<int:pk>/lectures/", views.CourseLecturesView.as_view()),

    path("course_students/", views.AllCourseStudentsListView.as_view()),
    path("course_students/<int:pk>/", views.CourseStudentsDetailView.as_view()),

    path("course_teachers/", views.AllCourseTeachersListView.as_view()),
    path("course_teachers/<int:pk>/", views.CourseTeachersDetailView.as_view()),

    path("lectures/", views.LecturesListCreateView.as_view()),
    path("lectures/<int:pk>/", views.LecturesDetailView.as_view()),
    path("lectures/<int:pk>/homeworks/", views.HomeworkListView.as_view()),

    path("marks/<int:pk>/", views.MarkDetailView.as_view()),
    path("marks/", views.MarkListCreateView.as_view()),

    path("comments/<int:pk>/", views.CommentDetailView.as_view()),
    path("comments/", views.CommentListCreateView.as_view()),

    path("students/<int:pk>/courses/", views.StudentCourseList.as_view()),
    path("students/<int:pk>/homeworks/", views.StudentHomeworkListView.as_view()),
    path("students/<int:pk_student>/lectures/<int:pk_lecture>/homeworks/", views.StudentLectureHomeworksListCreateView.as_view()),
    #path("students/<int:pk_student>/lectures/<int:pk_lecture>/homeworks/<int:pk_homework>/", views.StudentLectureHomeworkDetailView.as_view()),

    path("teachers/<int:pk>/courses/", views.HomeworkDetailView.as_view()),

    path("students/<int:pk>/", views.StudentDetailView.as_view()),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view())
]
