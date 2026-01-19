from django.urls  import path
from .views import ListCreateViews,UpdateViews


urlpatterns = [
    path('teachers/',ListCreateViews.as_view(),name="teachers"),
    path('teachers/<int:id>/',UpdateViews.as_view(),name="teachers")
]
