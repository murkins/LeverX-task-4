from django.contrib.auth.models import User
from django.db import models


class Persona(models.Model):
    user = models.OneToOneField(User,
                                related_name='persona_rel',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{"Teacher" if self.is_teacher else "Student"}: username={self.user.username}; name={self.name}'


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class CourseStudent(models.Model):
    persona = models.ForeignKey(Persona,
                                on_delete=models.CASCADE,
                                related_name="student_courses")
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name="course_students")

    def __str__(self):
        return f'{self.persona}; Course={self.course};'


class CourseTeacher(models.Model):
    persona = models.ForeignKey(Persona,
                                on_delete=models.CASCADE,
                                related_name="teacher_courses",
                                null=True)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name="course_teachers")

    def __str__(self):
        return f'{self.persona}, Course={self.course}'


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    #present_file_name = models.FileField(upload_to='uploads/')
    present_file_name = models.CharField(max_length=200)
    hometask = models.TextField(blank=False)
    course = models.ForeignKey(Course, related_name='course_lectures', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Homework(models.Model):
    solution_link = models.CharField(max_length=500)
    student_user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, related_name="homeworks", on_delete=models.CASCADE)

    def __str__(self):
        return f"Homework Student: {self.student_user.name}, Solution: {self.solution_link}, Lecture: {self.lecture.title}"


class Mark(models.Model):
    homework = models.OneToOneField(Homework, related_name='rel_mark', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.value}'


class Comment(models.Model):
    body = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, related_name='comments', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'User: {self.user.name} Text: {self.body}'
