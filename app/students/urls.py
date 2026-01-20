from django.urls import path
from .views import StudentLisCreateView,StudentRetrievUpdateView


urlpatterns = [
    path('students/',StudentLisCreateView.as_view(),name='students'),
    path('students/<int:id>/',StudentRetrievUpdateView.as_view(),name='students_id')
]
