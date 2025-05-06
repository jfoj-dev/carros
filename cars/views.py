from django.shortcuts import render
from cars.models import Car  

# Create your views here.

def cars_view(request):
   print(request.GET.get('search'))   
   
   cars = Car.objects.all()
   

   return render(
       request, 
       'cars.html',
       {'cars': cars}
    )