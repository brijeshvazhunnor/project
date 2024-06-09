from django.db import models

# Create your models here.
class Exam(models.Model):
    sem=models.IntegerField()
    year=models.IntegerField()
    month=models.CharField(max_length=20)
    grad_level=models.CharField(max_length=20)

    def __str__(self):
        return self.grad_level

class Department(models.Model):
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name


class Programme(models.Model):
    pgm_id = models.IntegerField(unique=True)
    pgm_name = models.CharField(max_length=50)
    grad_level = models.ForeignKey(Exam,on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.pgm_name

class Course(models.Model):
    course_id = models.IntegerField()
    course_title = models.CharField(max_length=50)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    Syllabus_year = models.IntegerField()
    course_code= models.CharField(max_length=20)

    def __str__(self):
        return self.course_title

class ExamTimeTable(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    date=models.DateField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    course_id = models.ForeignKey(Course,models.CASCADE)

    def __str__(self):
        return self.exam


class teacherTable(models.Model):
    teacher_id=models.IntegerField()
    dept_id=models.IntegerField()
    name=models.CharField(max_length=40)
    designation=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class room(models.Model):
    room_id=models.IntegerField()
    room_no=models.IntegerField()
    no_of_coloums=models.IntegerField()
    location=models.CharField(max_length=40)

    def __str__(self):
        return self.room_id

class dutyAllotment(models.Model):
    teacher_id=models.ForeignKey(teacherTable,on_delete=models.CASCADE)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date=models.DateField()
    room_id=models.ForeignKey(room,on_delete=models.CASCADE)
    

class preferTable(models.Model):
    teacher_id=models.IntegerField()
    exam_id=models.IntegerField()
    date=models.DateField()


class Timetable(models.Model):
    exam_id=models.IntegerField()
    date=models.DateField()
    course_id=models.IntegerField()

class Optedtb(models.Model):
    date=models.DateField()
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=40)