from django.urls import path
from . import views

urlpatterns = [
    path('manga_list/', views.mangaListView, name='mangaList'),
    path('manga_detail/<int:id>/', views.mangaDetailView, name='detail'),
]

