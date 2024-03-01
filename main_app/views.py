from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dino, Milestone
from .forms import VaccineForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dino_index(request):
  dinos = Dino.objects.all()
  return render(request, 'dinos/index.html', { 'dinos' : dinos})

def dino_detail(request, dino_id):
  dino = Dino.objects.get(id=dino_id)
  vaccine_form = VaccineForm()
  return render(request, 'dinos/detail.html', { 
    'dino' : dino, 'vaccine_form': vaccine_form
    })

class DinoCreate(CreateView):
  model = Dino
  fields = ['name', 'dinosaurType', 'age', 'diet', 'length', 'height']
  success_url = '/dinos/index'

def add_vaccine(request, dino_id):
  form = VaccineForm(request.POST)
  if form.is_valid():
    new_vaccine = form.save(commit=False)
    new_vaccine.dino_id = dino_id
    new_vaccine.save()
  return redirect('dino-detail', dino_id=dino_id)

class MilestoneCreate(CreateView):
  model = Milestone
  fields = '__all__'

class MilestoneList(ListView):
  model = Milestone

class MilestoneDetail(DetailView):
  model = Milestone

class MilestoneUpdate(UpdateView):
  model = Milestone
  fields = ['name', 'description']

class MilestoneDelete(DeleteView):
  model = Milestone
  success_url = '/milestones/'