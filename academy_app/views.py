from django.core import paginator
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from academy_app.models import CourseLectures, Courses, Curriculum, Enroll, Payment, PaymentDetail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# homepage
def index(request):
    courses = Courses.objects.all()[:4]
    context = {
        'courses': courses,
    }
    return render(request, 'index.html', context)


# courses page
def courses(request):
    courses = Courses.objects.all()
    paginator = Paginator(courses, 4)
    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)

    context = {
        'courses': page,
        'pages': paginator
    }
    return render(request, 'courses.html', context)


# search view
def search(request):
    if request.method == 'GET':
        query = request.GET['q']
        search = Q(course_title__icontains=query) | Q(description__icontains=query) | Q(prerequisites__icontains=query)
        result = Courses.objects.all().filter(search).distinct()

        paginator = Paginator(result, 8)
        page = request.GET.get('page')

        try:
            search_list = paginator.page(page)
        except PageNotAnInteger:
            search_list = paginator.page(1)
        except EmptyPage:
            search_list = paginator.page(paginator.num_pages)


        context = {
            'query' : query,
            'result' : search_list,
            'pages' : paginator
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

# course detail page
def course_detail(request, id):
    try:
        course = Courses.objects.get(pk=id)
        lectures = CourseLectures.objects.filter(course=course)
    except:
        messages.add_message(request, messages.WARNING, "something went wrong!")
        return redirect("/courses")

    curriculum = Curriculum.objects.filter(course=course)
    
    context = {
            'course': course,
            'lectures': lectures,
            'curriculum': curriculum
        }
    if request.user.is_authenticated:

        enroll = Enroll.objects.filter(course=course, user=request.user)
        if enroll.count() > 0:
            context['enrolled'] = True
            print(enroll.count())
            
    
    return render(request, 'course-detail.html', context)


# enroll page
@login_required(login_url="/login")
def enroll(request, course_id):
    course = Courses.objects.get(pk=course_id)
    return render(request, 'enroll.html', {'course': course})

# proceed enroll

@require_http_methods(["POST"])
@login_required(login_url="/login")
def enroll_proceed(request, course_id, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        course = Courses.objects.get(pk=course_id)

        # checking user is already enrolled or not
        try:
            enroll_check = Enroll.objects.get(course=course, user=request.user)
            messages.add_message(request, messages.INFO, "You have already inrolled in this course.")
            return redirect('/dashboard/enrolled')
        except:

            # entering data to the Enroll table
            enroll = Enroll()
            enroll.user = user
            enroll.course= course
            enroll.first_name = request.POST['fname']
            enroll.last_name = request.POST['lname']
            enroll.email = request.POST['email']
            enroll.phone = request.POST['phone']
            enroll.address = request.POST['address']
            enroll.save()
            
            return redirect('/payment/course/'+str(course_id)+'/'+str(enroll.id)+'/'+str(user_id))
    else:
        return redirect('/enroll/course/'+str(course_id))

# payment page
def payment(request, course_id, enroll_id, user_id):
    try:
        course = Courses.objects.get(pk=course_id)
        enroll = Enroll.objects.get(pk=enroll_id)
    except:
        messages.add_message(request, messages.SUCCESS, "something went wrong!")
        return redirect('/dashboard/enrolled') 
    if request.method == 'POST':
        # payment detail
        payment_detail = PaymentDetail()
        payment_detail.bank = request.POST['bank']
        payment_detail.card_number = request.POST['card-number']
        payment_detail.expiry = request.POST['expiry-date']
        payment_detail.holder_name = request.POST['name']
        payment_detail.save()


        user = User.objects.get(pk=user_id)
        # billing payment
        payment = Payment()
        payment.user = user
        payment.course = course
        payment.payment_status = True
        payment.total_amount = course.fee
        payment.payment_detail = payment_detail
        payment.save()

        # adding payment id to Enroll
        enroll.payment_id = payment.id
        try:
            enroll.save()
        except:
            messages.add_message(request, messages.ERROR, "something went wrong!")
            



        messages.add_message(request, messages.SUCCESS, "enrolled successfully!")
        return redirect('/dashboard/enrolled') 

    else:
        context = {
            'course' : course,
            'enroll' : enroll,
        }
        return render(request, 'payment.html', context)


# login page
def login_view(request):
    # redirectiong to Dashboard if user is already logged in
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, "You are already logged in.")
        return redirect("/dashboard")

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user_obj = User.objects.get(email = email)
        except:
            messages.add_message(request, messages.WARNING, "user doesn't esixts!")
            return redirect("/login")

        username = user_obj.username
    
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in successfully!")
            return redirect("/dashboard")
        else:
            messages.add_message(request, messages.ERROR, "Incorrect Credentials")
            return redirect("/login")
    else:
        return render(request, 'login.html')

# logout
@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged out successfully!")
    return redirect("/login")
    
# signup page
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        name = fullname.split()
        first_name = name[0]
        last_name = ' '.join(name[1:])
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm-password']

        # checking user is already is exists or not
        try:
            user_check = User.objects.get(username=username)
            messages.add_message(request, messages.ERROR, "Username is not available!")
            return redirect('/signup')
        except:
            try:
                email_check = User.objects.get(email=email)
                messages.add_message(request, messages.ERROR, "Email is already in use!")
                return redirect('/signup')
            except:
                if password == cpassword:
                    user = User.objects.create_user(username, email, password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    messages.add_message(request, messages.SUCCESS, "Account created successfully!")
                    return redirect("/login")
                else:
                    messages.add_message(request, messages.ERROR, "Password didn't match!")
                    return redirect("/signup")
    else:
        return render(request, 'signup.html')



# FAQ
def faq(request):
    return render(request, 'faq.html')