from django.urls import path
from . import views


urlpatterns = [
    path("teachers", views.see_teacher, name="see-teacher"),
]
