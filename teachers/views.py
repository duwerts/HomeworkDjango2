from django.shortcuts import render, redirect
from .models import Teacher, Group
from .forms import TeacherForm, GroupForm


def create_teachers(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/teachers/")
    else:
        form = TeacherForm()

    return render(request, "teacher_form.html", {"form": form})


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/groups/")
    else:
        form = GroupForm()

    return render(request, "group_form.html", {"form": form})


def list_groups(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})
