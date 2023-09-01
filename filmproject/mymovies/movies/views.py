from django.shortcuts import render, redirect

from .forms import movieform
from .models import movielist
# Create your views here.
def index(request):
    movie=movielist.objects.all()
    context={
        'movie': movie
    }
    return render(request,'index.html',context)

def detail (request,movieid):
    movie=movielist.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':movie})

def update (request,id):
    movie=movielist.objects.get(id=id)
    forms=movieform(request.POST or None,instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'update.html',{'movie':movie,'forms':forms})

def delete(request,id):
    if request.method == 'POST':
        movie=movielist.objects.get(id=id)
        movie.delete()
        return redirect ('/')
    return render(request,'delete.html')

def add(request):
    if request.method =="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=movielist(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect ('/')
    return render(request,'add.html')
