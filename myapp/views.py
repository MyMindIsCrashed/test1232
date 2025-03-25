from django.shortcuts import render
from .models import Doctors


def index(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')


def test(request):

    doc = Doctors.objects.all()

    return render(request, 'myapp/test.html', {'doc' : doc})
