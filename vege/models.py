from django.db import models
class Department(models.Model):
    department=models.CharField(max_length=120)
    def __str__(self):
        return self.department
    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id=models.CharField(max_length=120)
    def __str__(self):
        return self.student_id        

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    def __str__(self):
        return self.subject_name     
class Students(models.Model):
    department=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE,null=True, blank=True)
    student_id=models.OneToOneField(StudentID,related_name="studentid",on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['name']
class StudentsMark(models.Model):
    students=models.ForeignKey(Students,related_name="studentsmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()
    
    def __str__(self):
        return f"{self.students.name} {self.subject.subject_name}"
    
    class Meta:
        unique_together=('students','subject')