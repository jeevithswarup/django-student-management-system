from django.shortcuts import render
from django.db.models import Q,Sum
from django.core.paginator import Paginator
from vege.models import *
def receipe(request):
    return render(request,'receipe.html')


def get_students(request):
    queryset=Students.objects.all()
    if request.GET.get('search'):
     search=request.GET.get('search')
     queryset=Students.objects.filter(
        Q(student_id__student_id__icontains =search)|
        Q(department__department__icontains=search)|
        Q(name__icontains=search)|
        Q(age__icontains=search)|
        Q(email__icontains=search)
        )
    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "data.html", {"page_obj": page_obj})


def subject_mark(request,student_id):
    queryset=StudentsMark.objects.filter(students__student_id__student_id = student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    ranks=Students.objects.annotate(marks=Sum('studentsmarks__marks')).order_by('-marks')
    rank_position=None
    count=1 
    for r in ranks:
     if r.student_id.student_id==student_id:
        rank_position=count
        break
     count+=1
    return render(request, "result.html", {"queryset":queryset,'total_marks': total_marks,'rank_position':rank_position})

    


