from django.db import models

class CourseModel(models.Model):
    Course_Id = models.AutoField(primary_key=True)
    Course_Name = models.CharField(max_length=50,unique=True)
    Faculty = models.CharField(max_length=50)
    Date = models.DateField()
    Time = models.CharField(max_length=50)
    Fee = models.FloatField()
    Duration = models.CharField(max_length=50)

class StudentModel(models.Model):
    Student_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=60)
    Contactno = models.IntegerField(unique=True)
    Email = models.EmailField(max_length=100,unique=True)
    Password = models.CharField(max_length=50)

class stud_course(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.IntegerField()
    cid = models.IntegerField()


