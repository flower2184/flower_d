from django.urls import path
from . import views

app_name = 'gameboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:games_id>/', views.detail, name='detail'),
    path('answer/create/<int:games_id>/', views.answer_create, name='answer_create'),
    path('games/create/', views.games_create, name='games_create'),
    path('games/delete/<int:games_id>/', views.games_delete, name='games_delete'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

]