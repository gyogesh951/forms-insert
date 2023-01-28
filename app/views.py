from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_form(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insertform is success')

    return render(request,'insert_form.html')