from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Dino, Milestone
from .forms import VaccineForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def about(request):
  return render(request, 'about.html')

@login_required
def dino_index(request):
  dinos = Dino.objects.filter(user=request.user)
  return render(request, 'dinos/index.html', { 'dinos' : dinos})

@login_required
def dino_detail(request, dino_id):
  dino = Dino.objects.get(id=dino_id)
  milestones_dino_doesnt_have = Milestone.objects.exclude(id__in = dino.milestones.all().values_list('id'))
  vaccine_form = VaccineForm()
  return render(request, 'dinos/detail.html', { 
    'dino' : dino, 'vaccine_form': vaccine_form, 'milestones': milestones_dino_doesnt_have
    })

class DinoCreate(CreateView):
  model = Dino
  fields = ['name', 'dinosaurType', 'age', 'diet', 'length', 'height']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/dinos/index'

class DinoUpdate(LoginRequiredMixin, UpdateView):
  model = Dino
  fields = ['dinosaurType', 'age', 'diet', 'length', 'height']

class DinoDelete(LoginRequiredMixin, DeleteView):
  model = Dino
  success_url = '/dinos/'

@login_required
def add_vaccine(request, dino_id):
  form = VaccineForm(request.POST)
  if form.is_valid():
    new_vaccine = form.save(commit=False)
    new_vaccine.dino_id = dino_id
    new_vaccine.save()
  return redirect('dino-detail', dino_id=dino_id)

class MilestoneCreate(LoginRequiredMixin, CreateView):
  model = Milestone
  fields = '__all__'

class MilestoneList(LoginRequiredMixin, ListView):
  model = Milestone

class MilestoneDetail(LoginRequiredMixin, DetailView):
  model = Milestone

class MilestoneUpdate(LoginRequiredMixin, UpdateView):
  model = Milestone
  fields = ['name', 'description']

class MilestoneDelete(LoginRequiredMixin, DeleteView):
  model = Milestone
  success_url = '/milestones/'

@login_required
def assoc_milestone(request, dino_id, milestone_id):
  # Note that you can pass a milestone's id instead of the whole object
  Dino.objects.get(id=dino_id).milestones.add(milestone_id)
  return redirect('dino-detail', dino_id=dino_id)


