from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks, name='parks-index'),
    path('parks/<int:park_id>/', views.park_detail, name='park-detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='park-create'),
    path('park/<int:pk>/update', views.ParkUpdate.as_view(), name='park-update'),
    path('park/<int:pk>/delete', views.ParkDelete.as_view(), name='park-delete')
]
