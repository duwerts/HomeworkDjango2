from django.urls import path
from . import views


urlpatterns = [
    path("teacher/", views.create_teachers, name="create_teachers"),
    path("teachers/", views.list_teachers, name="list_teachers"),
    path("group/", views.create_group, name="create_group"),
    path("groups/", views.list_groups, name="list_groups"),
]
