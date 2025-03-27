from django.shortcuts import render
from .models import Doctors
from django.db.models import Q 
from django.core.paginator import Paginator


def index(request):
    search_query = request.GET.get('search', '')
    filter_job = request.GET.get('job', '')


   
    doctors = Doctors.objects.filter(
        Q(first_name__icontains=search_query) | 
        Q(last_name__icontains=search_query) | 
        Q(job_type__icontains=search_query)
    )

    if filter_job:
        doctors = doctors.filter(job_type=filter_job)

    paginator = Paginator(doctors, 6)  
    page_number = request.GET.get('page')  # Получаем номер текущей страницы из GET-запроса
    page_obj = paginator.get_page(page_number) 

    return render(request, 'myapp/index.html', {
        'page_obj': page_obj,  # Передаём объект пагинации в шаблон
        'search_query': search_query,
        'filter_job': filter_job,
    })



def about(request):
    return render(request, 'myapp/about.html')

