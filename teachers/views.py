from faker import Faker
from django.http import JsonResponse
from .models import Teacher


fake = Faker()


def see_teacher(request):
    teacher = Teacher.objects.all()
    return JsonResponse((teacher))
