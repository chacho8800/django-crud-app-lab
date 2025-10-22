from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks, name='parks-index'),
    path('parks/<int:park_id>/', views.park_detail, name='park-detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='park-create'),
    path('parks/<int:pk>/update', views.ParkUpdate.as_view(), name='park-update'),
    path('parks/<int:pk>/delete', views.ParkDelete.as_view(), name='park-delete'),
    path('parks/<int:park_id>/add-animal/', views.add_animal, name='add-animal'),
        
    path("activity/create/", views.ActivityCreate.as_view(), name="activity-create"),
    path("activity/<int:pk>/", views.ActivityDetail.as_view(), name="activity-detail"),
    path('activity/<int:pk>/delete', views.ActivityDelete.as_view(), name='activity-delete'),
    path('activity/<int:pk>/update', views.ActivityUpdate.as_view(), name='activity-update'),
    path("activity/", views.ActivityList.as_view(), name="activity-index"),
    
    path("animal/<int:animal_id>/", views.animal_detail, name="animal-detail"),
    path('animal/<int:pk>/delete', views.AnimalDelete.as_view(), name='animal-delete'),
    path('animal/<int:pk>/update', views.AnimalUpdate.as_view(), name='animal-update'),
    path('animals/', views.AnimalsList.as_view(), name='animals-index')
]
