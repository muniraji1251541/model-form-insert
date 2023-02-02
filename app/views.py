from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def insert_topic(request):
    to=Model_Topic()
    d={'form':to}
    if request.method=='POST':
        fd=Model_Topic(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('Topic data is inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    mo=Model_Webpage()
    d={'form':mo}
    if request.method=='POST':
        wd=Model_Webpage(request.POST)
        if wd.is_valid():
            wd.save()
            return HttpResponse('Webpage data is inserted')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    ao=Model_Access()
    d={'form':ao}
    if request.method=='POST':
        ad=Model_Access(request.POST)
        if ad.is_valid():
            ad.save()
            return HttpResponse('Accessrecord data is inserted')
    return render(request,'insert_access.html',d)