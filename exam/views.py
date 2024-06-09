from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group,User
@csrf_exempt
def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('hello')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'exam/login.html')   



# Create your views here.
@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Chief').exists():
            return render(request,'exam/chief.html')
        elif request.user.groups.filter(name='Teacher').exists():
            return render(request,'exam/teacher.html')
        elif request.user.groups.filter(name='Office').exists():
            return render(request,'exam/office.html')
        elif request.user.is_superuser:
            return render(request,'exam/home.html')
    


class ExamView(CreateView):
    model = Exam
    fields = "__all__"

    def get_success_url(self):
        return reverse('hello')


class ExamTimeTableView(CreateView):
    model = ExamTimeTable
    fields = "__all__"

    def get_success_url(self):
        return reverse('ExamTimeTable')
    

class teacherTableView(CreateView):
    model = teacherTable
    fields = "__all__"

    def get_success_url(self):
        return reverse('teacherTable')
    
class dutyAllotmentView(CreateView):
    model = dutyAllotment
    fields = "__all__"

    def get_success_url(self):
        return reverse('dutyAllotment')
    
class preferTableView(CreateView):
    model = preferTable
    fields = "__all__"

    def get_success_url(self):
        return reverse('preferTable')
    
class CourseTableView(CreateView):
    model = Course
    fields = "__all__"

    def get_success_url(self):
        return reverse('Course')


def cheifpage(request):
    exams = Exam.objects.all()
    print(list(exams))
    return render(request, 'exam/cpage.html', {'exams': exams})


def timetable(request,pk):
    exam={
        'exam':Exam.objects.filter(id=pk)
    }
    course={
        'course':Course.objects.all()
    }
    return render(request,'exam/tb.html',{**exam,**course})

def tbstore(request):
    if request.method=='POST':
        exam_id=request.POST.get('exam_id')
        date=request.POST.get('date')
        courses=request.POST.getlist('course')
        course_id=courses[0].split(':')[0]
        print(date)
        time_tb=Timetable(exam_id=exam_id,date=date,course_id=course_id)
        time_tb.save()

        return HttpResponse('ok')

def prefer(request):
    timetb={
        'timetb':Timetable.objects.all()
    }

    return render(request,'exam/prefer.html',timetb)

def opted(request):
    if request.method=='POST':
        options=request.POST.getlist('option')
        for i in options:
            user_id,date=i.split('_')
            user_name=User.objects.get(id=user_id).username
            date_obj = datetime.strptime(date, '%B %d, %Y')
            formatted_date = date_obj.strftime('%Y-%m-%d')
            op=Optedtb(user_id=user_id,date=formatted_date,user_name=user_name)
            op.save()
        return HttpResponse('ok')

def allot(request):
    choices={
        'choices':Optedtb.objects.all()
    }
    if request.method=="POST":
        date=request.POST.get('date')
        date_obj = datetime.strptime(date, '%B %d, %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        selected_date={
            'selected_date':Optedtb.objects.filter(date=formatted_date)
        }
        teachers={
            'teachers':User.objects.filter(groups__name='Teacher')
        }
        return render(request,'exam/allot.html',{**teachers,**selected_date})
    return render(request,'exam/allot.html',choices)