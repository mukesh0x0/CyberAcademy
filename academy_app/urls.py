from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.courses, name="courses"),
    path('course/detail/<int:id>/', views.course_detail, name='course detail'),
    path('enroll/course/<int:course_id>', views.enroll, name='enroll'),
    path('enroll/proceed/<int:course_id>/<int:user_id>', views.enroll_proceed, name='enroll'),
    path('payment/course/<int:course_id>/<int:enroll_id>/<int:user_id>', views.payment, name='payment'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name="logout"),
    path('faq', views.faq, name="FAQ"),
    path('search', views.search, name="search"),
]