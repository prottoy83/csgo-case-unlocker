from django.shortcuts import render
from .models import case,item
from django.shortcuts import render,get_object_or_404
import random


def index(request):
    case_set=case.objects.all()
    context={'case':case_set}
    return render(request,"index.html",context)
def result(request,id):
    data=get_object_or_404(case,id=id)
    value=random.randint(1,150)
    if value>=1 and value<=10:
        sign="rare"
    elif value>=11 and value<=30:
        sign="low"
    elif value>=31 and value<=60:
        sign="medium"
    elif value>=61 and value<=100:
        sign="high"
    else:
        sign="extreme"


    lol=item.objects.filter(case__id=id).filter(probability=sign)
    result=random.choice(lol)
    print(result)
    print(sign)
    context={'data':data,'result':result}
    return render(request,"results.html",context)

     