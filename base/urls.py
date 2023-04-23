from django.contrib import admin
from django.urls import path
from .views import landing, causes, calculator, bot#, evaluation
from . import views 

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.landing, name="home"), 
  path('causes', views.causes, name="causes"), 
  path('calculator', views.bot, name="calculator"),
]