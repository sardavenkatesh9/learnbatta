from django.urls import path
from . import views

urlpatterns = [
    path('movie-create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('movie-list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/detail/', views.MovieRetrieveView.as_view(), name='movie_retrieve'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie_update'),
]
