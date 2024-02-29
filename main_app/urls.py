from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dinos/index', views.dino_index, name='dino-index'),
  path('dinos/<int:dino_id>/', views.dino_detail, name='dino-detail'),
  path('dinos/create/', views.DinoCreate.as_view(), name='dino-create')
]


# The part <int:dino_id> specifies that Django should capture an integer value from the URL and pass it as the dino_id parameter to the dino_detail view function.

# When a request is made to a URL matching this pattern, such as /dino/5/, Django will extract the value 5 from the URL and pass it as the dino_id parameter to the dino_detail view function.