from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.
def Quijote(request):
     context={}
     return render(request, 'dashboard.html', context)
