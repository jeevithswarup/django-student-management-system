from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Students(models.Model):
    Student_name=models.CharField(max_length=150)
    student_email=models.EmailField(unique=True,null=True,blank=True)
    student_age=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(35)])
