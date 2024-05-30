from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_listing, name='movie_listing'),
    path('movie/<int:pk>/delete/', views.delete_movie, name='delete_movie'),
    path('detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('update/<int:pk>/', views.update_movie, name='update_movie'),
    path('create/', views.create_movie, name='create_movie'),

]
