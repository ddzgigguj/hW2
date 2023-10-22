from django.urls import path
from . import views

urlpatterns = [
    path('comix_list/', views.comixListView, name='comixList'),
    path('comix_detail/<int:id>/', views.mangaDetailView, name='detail'),
]
