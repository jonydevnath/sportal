from django.db import models
import datetime

# Create your models here.
from django.db import models
import datetime

class Enroll(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=100, default='', blank=False)
    days = models.CharField(max_length=100, default='', blank=False)
    class_time = models.CharField(max_length=100, default='', blank=False)
    room_no = models.CharField(max_length=100, default='', blank=False)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.course_name}"
    
class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    notice = models.CharField(max_length=500, default='', blank=False)

    def __str__(self):
        return f"{self.notice}"

class Routine(models.Model):
    id = models.BigAutoField(primary_key=True)
    exam_date = models.CharField(max_length=100, default='', blank=False)  # Change as per your need
    exam_time = models.CharField(max_length=100, default='', blank=False)
    course_code = models.CharField(max_length=100, default='', blank=False)
    course_name = models.CharField(max_length=100, default='', blank=False)
    course_credit = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    course_type = models.CharField(max_length=100, default='', blank=False)  # Assuming it's a string
    room_no = models.CharField(max_length=100, default='', blank=False)

    def __str__(self):
        return f"{self.course_name}"