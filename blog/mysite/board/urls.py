from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:context_id>/', views.detail, name='detail'),
    
]
