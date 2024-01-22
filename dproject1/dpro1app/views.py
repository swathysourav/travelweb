from django.shortcuts import render
from . models import travel
from . models import meetteam
from django.http import HttpResponse
# Create your views here.
def demo(request):
    obj=travel.objects.all()
    obj1=meetteam.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
