from django.urls  import path
from .views import ListCreateViews


urlpatterns = [
    path('teachers/',ListCreateViews.as_view(),name="teachers")
]
