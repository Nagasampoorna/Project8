from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib import messages
from app8.models import CourseModel,StudentModel,stud_course
from app8.forms import CourseForm,StudentForm

def showIndex(request):
    return render(request,'index.html')
def save_admin(request):
    uname = request.POST.get('t1')
    pword = request.POST.get('t2')
    if uname == "sampoorna" and pword == "sam123":
         return render(request,'schedule_class.html',{'name':uname})
    else:
         messages.error(request,"Invalid Username And Password")
         return redirect('index')
def schedule_class(request):
    cf = CourseForm()
    return render(request,'schedule_class.html',{"form":cf})
def view_class(request):
    res = CourseModel.objects.all()
    return render(request,'view_class.html',{'data':res})
def save_course(request):
    cf = CourseForm(request.POST)
    if cf.is_valid():
        cf.save()
        messages.success(request, "Successfully Registered")
        return redirect('schedule_class')
    else:
        messages.error(request,"Registration Is Failed")
        return redirect('schedule_class')
def update_view(request):
   id = request.GET.get('Course_Name')
   res = CourseModel.objects.get(Course_Name=id)
   return render(request,'update_view.html',{'data':res})
def update_schedule(request):
    id = request.POST.get('c1')
    na = request.POST.get('c2')
    fa = request.POST.get('c3')
    date = request.POST.get('c4')
    time = request.POST.get('c5')
    fee = request.POST.get('c6')
    dur = request.POST.get('c7')
    CourseModel.objects.filter(Course_Id=id).update(Course_Name=na,Faculty=fa, Date=date, Time=time, Fee=fee, Duration=dur)
    messages.success(request,'Successfully Updated')
    return redirect('view_class')
def delete_view(request):
    cn = request.GET.get('id')
    CourseModel.objects.filter(id=cn).delete()
    messages.success(request,'Successfully Deleted')
    return redirect('view_class')
############# student page ########################
def student_register(request):
    std = StudentModel.objects.all()
    return render(request,'student_register.html',{'data':std})
def save_register_student(request):
    na = request.POST.get("n1")
    cn = request.POST.get("n2")
    ei = request.POST.get("n3")
    pw = request.POST.get("n4")
    StudentModel(Name=na, Contactno=cn, Email=ei, Password=pw).save()
    return redirect('student_register')
def student_login(request):
    return render(request,'student_login.html')
def student_page(request):
    un = request.POST.get('s1')
    ps = request.POST.get('s2')
    cor = CourseModel.objects.all()
    try:
        res = StudentModel.objects.get(Q(Email=un,Password=ps))
        request.session['Student_Id']=res.Student_Id
        return render(request,'student_page.html',{'data':res,'course':cor})
    except StudentModel.DoesNotExist:
        return render(request,'student_login.html',{'error':'Does not Exist'})

  #  usr = StudentModel.objects.filter(Email__in=[un]).all()
  #  for x in usr:
  #      if ps==x.Password:
  #          return render(request, "student_page.html")
  #  messages.error(request, "Invalid User")
  #  return redirect('student_log')

#def student_page(request):
 #   return render(request,'student_page.html')
def enrol_course(request):
    res = CourseModel.objects.all()
    return render(request,'enrol_course.html',{'data':res})
def enrolled(request):
    cid = request.GET.get('cid')
    sid = request.GET.get('sid')
    try:
        stud_course.objects.get(cid=cid,sid=sid)
        messages.error(request, "Already Enrolled")
        return redirect('enrol_course')
    except stud_course.DoesNotExist:
        stud_course(sid=sid, cid=cid).save()
        messages.success(request, "Enrolled Successfully")
        return redirect('enrol_course')

def view_enrolled_courses(request):
    sid = request.GET.get('sid')
    res = stud_course.objects.filter(sid=sid)
    coures = [CourseModel.objects.get(Course_Id=x.cid) for x in res]
    return render(request, 'view_enrolled_courses.html', {'data': coures})
def cancel_enrolled_courses(request):
    sid = request.GET.get('sid')
    sc = stud_course.objects.filter(sid=sid)
    data = [CourseModel.objects.get(Course_Id=x.cid) for x in sc]
    return render(request,'cancel_enrolled_courses.html', {'data': data})
def delete_enrol(request):
    cid = request.POST.get('cid')
    sid = request.POST.get('sid')
    stud_course.objects.get(cid=cid, sid=sid).delete()
    res = stud_course.objects.filter(sid=sid)
    data = [stud_course.objects.get(cid=x.cid) for x in res]
    return render(request,"cancel_enrolled_courses.html", {"data": data})
def logout(request):
    # del request.session['sid']
    return redirect('student_login')
def contact(request):
    return render(request,"contact.html")