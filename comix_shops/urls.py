from django.urls import path
from . import views

urlpatterns = [
    path('comix_list/', views.mangaListView, name='comixList'),
    path('comix_detail/<int:id>/', views.mangaDetailView, name='detail'),
]

