from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('dinos/index', views.dino_index, name='dino-index'),
  path('dinos/<int:dino_id>/', views.dino_detail, name='dino-detail'),
  path('dinos/create/', views.DinoCreate.as_view(), name='dino-create'),
  path('dinos/<int:pk>/update/', views.DinoUpdate.as_view(), name='dino-update'),
  path('dinos/<int:pk>/delete/', views.DinoDelete.as_view(), name='dino-delete'),
  path('dinos/<int:dino_id>/add-vaccine/', views.add_vaccine, name='add-vaccine'),
  path('milestones/create', views.MilestoneCreate.as_view(), name='milestone-create'),
  path('milestones/<int:pk>/', views.MilestoneDetail.as_view(), name='milestone-detail'),
  path('milestones/', views.MilestoneList.as_view(), name='milestone-index'),
  path('milestones/<int:pk>/update', views.MilestoneUpdate.as_view(), name='milestone-update'),
  path('milestones/<int:pk>/delete', views.MilestoneDelete.as_view(), name='milestone-delete'),
  # associate a toy with a dino (M:M)
  path('dinos/<int:dino_id>/assoc-milestone/<int:milestone_id>/', views.assoc_milestone, name='assoc-milestone'),
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.Home.as_view(), name='home'),
]


# The part <int:dino_id> specifies that Django should capture an integer value from the URL and pass it as the dino_id parameter to the dino_detail view function.

# When a request is made to a URL matching this pattern, such as /dino/5/, Django will extract the value 5 from the URL and pass it as the dino_id parameter to the dino_detail view function.