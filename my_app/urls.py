from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks, name='parks-index'),
    path('parks/<int:park_id>/', views.park_detail, name='park-detail')
]
