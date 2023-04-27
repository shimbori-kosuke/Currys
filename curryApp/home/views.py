from django.shortcuts import render

#from .models import 

def IndexView(request):
    context = {
        
    }
    return render(request, 'home/home.html', context)