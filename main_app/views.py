from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
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
  fields = '__all__'
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