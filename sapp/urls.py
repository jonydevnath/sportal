from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enroll/', views.enroll, name='enroll'),
    path('notice/', views.notice, name='notice'),
    path('routine/', views.routine, name='routine'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('homeworks/', views.homeworks, name='homeworks'),
    path('login/', views.login, name='login'),
]