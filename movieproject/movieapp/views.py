from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieForm
from . models import movie
# Create your views here.

def index(request):
    moviee = movie.objects.all()
    context={
        'movie_list':moviee
    }
    return render(request,'index.html',context)
    # return HttpResponse("HELLO")


def detail(request,movie_id):
    moviee=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':moviee})


def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        moviee=movie(name=name,desc=desc,year=year,img=img)
        moviee.save()
    return render(request,'add.html')


def update(request,id):
    moviee=movie.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=moviee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'moviee':moviee})


def delete(request, id, mov=None):
    if request.method=="POST":
        moviee=movie.objects.get(id=id)
        
        moviee.delete()
        return redirect('/')
    return  render(request,'delete.html')
