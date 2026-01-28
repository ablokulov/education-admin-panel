from django.urls import path
from .views import StudentListCreateView,StudentRetrieveUpdateView


urlpatterns = [
    path('students/',StudentListCreateView.as_view(),name='students'),
    path('students/<int:id>/',StudentRetrieveUpdateView.as_view(),name='students_id')
]
