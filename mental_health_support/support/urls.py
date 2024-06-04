from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('therapists/', views.therapist_list, name='therapist_list'),
    path('forum/', views.forum, name='forum'),
    path('register/', views.register, name='register'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointments, name='appointments'),
]
