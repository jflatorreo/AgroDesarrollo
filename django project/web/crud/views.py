from django.shortcuts import render, redirect
from .models import Semoviente

# Create your views here.

def index(request):
    semovientes = Semoviente.objects.all()
    context = {'semovientes': semovientes}
    return render(request, 'crud/index.html', context)

def create(request):
    semoviente = Semoviente(chapeta=request.POST['chapeta'], fecha_ingreso=request.POST['fecha_ingreso'])
    semoviente.save()
    return redirect('/')

def edit(request, id):
    semovientes = Semoviente.objects.get(id=id)
    context = {'semovientes': semovientes}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    semoviente = Semoviente.objects.get(id=id)
    semoviente.chapeta = request.POST['chapeta']
    semoviente.fecha_ingreso = request.POST['fecha_ingreso']
    semoviente.save()
    return redirect('/crud/')

def delete(request, id):
    semoviente = Semoviente.objects.get(id=id)
    semoviente.delete()
    return redirect('/crud/')