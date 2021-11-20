from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('enrolled', views.enrolled, name='enrolled'),
    path('setting', views.setting, name='setting'),
    path('course/<int:course_id>/learn/', views.learning, name='learning'),
]