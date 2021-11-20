from django.contrib.auth.models import User
from django.contrib import messages
from django.http import request
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render
from academy_app.models import CourseLectures, Courses, Enroll, Payment

# dashboard home
@login_required(login_url="/login")
def dashboard(request):
    print(request.user.username)
    ongoing = Enroll.objects.filter(user=request.user)
    
    return render(request, 'dashboard.html', {'ongoing': ongoing})


# enrolled courses
@login_required(login_url="/login")
def enrolled(request):
    ongoing = Enroll.objects.filter(user=request.user)
    return render(request, 'dash-enrolled.html', {'ongoing': ongoing})


# account
@login_required(login_url="/login")
def setting(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            user = User.objects.get(username=request.user.username)
            user.set_password(request.POST['password'])
            try:
                user.save()
            except:
                messages.add_message(request, messages.WARNING, "use numbes and symboles in your password")
                return render(request, 'setting.html')

            messages.add_message(request, messages.SUCCESS, "Passowrd changed successfylly!")
            authenticate(request, username=user.username, password=user.password)
            login(request, user)
            return redirect('/dashboard/setting')

        else:
            messages.add_message(request, messages.ERROR, "password didn't match!")
            return render(request, 'setting.html')

    else:
        return render(request, 'setting.html')

#learning page
@login_required(login_url="/login")
def learning(request, course_id):
    try:
        course = Courses.objects.get(pk=course_id)
        try:
            enrolled = Enroll.objects.filter(course=course, user=request.user)
            payment = Payment.objects.get(course=course, user=request.user)
            if payment.payment_status == False:
                return redirect("/payment/course"+str(course_id)+str(enrolled.id)+str(request.user.id))
        except:
            # pass
            return redirect('/course/detail/'+str(course_id))

        
        lectures = CourseLectures.objects.filter(course=course)
        if request.GET['chapter'] == '':
            lecture = lectures[0]
        else:
            lecture = CourseLectures.objects.get(id=request.GET['chapter'], course=course)

    except:
        return HttpResponse("something went woring")

    return render(request, 'learning.html', {'lecture': lecture, 'lectures': lectures})
