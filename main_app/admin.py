from django.contrib import admin
from .models import Dino, Vaccine, Milestone

# Register your models here.
admin.site.register(Dino)
admin.site.register(Vaccine)
admin.site.register(Milestone)