from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.mylogin,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('home/',views.home,name='hello'),
    path('exam/',views.ExamView.as_view(),name='exam'),
    path('timetable/',views.ExamTimeTableView.as_view(),name='timetable'),
    path('duty/',views.dutyAllotmentView.as_view(),name='dutyAllotment'),
    path('prefer/',views.preferTableView.as_view(),name='preferTable'),
    path('course/',views.CourseTableView.as_view(),name='course'),
    path('cpage/',views.cheifpage,name='cpage'),
    path('tb/<int:pk>',views.timetable,name='timetable'),
    path('tbstore',views.tbstore,name='tbstore'),
    path('timetb',views.prefer,name='timetb'),
    path('opted',views.opted,name='opted'),
    path('allot',views.allot,name='allot')
]

