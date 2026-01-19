from django.urls import path
from .views import GroupsListCreateView,GroupsUpdateDistroyView


urlpatterns = [
    path('groups/',GroupsListCreateView.as_view(),name='groups'),
    path('groups/<int:id>/',GroupsUpdateDistroyView.as_view(),name='groups')
]
