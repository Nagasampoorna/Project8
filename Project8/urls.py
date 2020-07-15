"""Project8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app8 import views
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.showIndex, name='index'),
        path('save_admin/', views.save_admin, name='save_admin'),
        path('schedule_class/', views.schedule_class, name='schedule_class'),
        path('save_course/', views.save_course, name='save_course'),
        path('view_class/', views.view_class, name='view_class'),
        path('update_view/', views.update_view, name='update_view'),
        path('update_schedule/', views.update_schedule, name='update_schedule'),
        path('delete_view/', views.delete_view, name='delete_view'),
         ############ student page ###################
        path('student_register/',views.student_register,name='student_register'),
        path('save_register_student/',views.save_register_student,name='save_register_student'),
        #path('student_log/',views.student_log,name='student_log'),
        path('student_login/', views.student_login, name='student_login'),
        path('student_page/',views.student_page,name='student_page'),
        path('enrol_course/', views.enrol_course, name='enrol_course'),
        path('enrolled/',views.enrolled,name='enrolled'),

        path('view_enrolled_courses/', views.view_enrolled_courses, name='view_enrolled_courses'),
        path('cancel_enrollled_courses/', views.cancel_enrolled_courses, name='cancel_enrolled_courses'),
        path('delete_enrol/', views.delete_enrol, name='delete_enrol'),
        path('update_course/',views.update_course,name='update_course'),
        path('contact/',views.contact,name='contact'),
        path('logout/',views.logout,name='logout'),


]
