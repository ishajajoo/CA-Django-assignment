from . import views
from django.urls import path

urlpatterns = [
   path('Homepage/', views.homepage),
   path('Indexpage/', views.index),
   path('all-student/', views.AllStudentDetails),
   path('student-details/<int:pk>', views.SingleStudentDetails)
 ]