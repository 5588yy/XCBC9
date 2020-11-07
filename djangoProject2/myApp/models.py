from django.db import models


# Create your models here.
# login_student
# login_teacher
# sum
class student(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)


class teacher(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)


class reasult1(models.Model):
    groupname = models.CharField(primary_key=True, max_length=15)
    votenum = models.CharField(max_length=15)
