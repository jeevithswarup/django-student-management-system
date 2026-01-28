from faker import Faker
fake= Faker()
from vege.models import*
import random

def subject_marks_create(n):
     try:
        studentobjs=Students.objects.all()
        for student in studentobjs:
          subjectobjs=Subject.objects.all()
          for subject in subjectobjs:
            StudentsMark.objects.create(
              students=student,
              subject=subject,
              marks=random.randint(30,99),
            )
     except Exception as e:
       print(e)


def seed_db(n=10)->None:
 try: 
  for i in range(n): 
    department_objs=Department.objects.all()
    random_index=random.randint(0,len(department_objs)-1)
  
    department=department_objs[random_index]
    student_id=f"230303{random.randint(1060,1650)}"
    name=fake.name()
    age=random.randint(20,30)
    email=fake.email()
    student_id_objs=StudentID.objects.create(student_id=student_id)

    student_obj=Students.objects.create(

        department=department,
        student_id=student_id_objs,
        name =name,
        age=age,
        email=email,
        
    )
 except Exception as e:
  print(e)