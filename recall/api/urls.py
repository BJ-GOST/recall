from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('create-note', views.createNote, name='create-note'),
    path('note-detail/<str:pk>/', views.noteDetail, name='note-detail'),
    path('update-note/<str:pk>/', views.updateNote, name='update-note'),
    path('delete-note/<str:pk>/', views.deleteNote, name='delete'),
    path('get-notes/', views.get_original_notes, name='get-notes')
]