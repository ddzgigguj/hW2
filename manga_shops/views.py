from django.shortcuts import render, get_object_or_404
from . import models

def mangaListView(request):
    manga_value = models.Manga_shops,object.all()
    html_name = 'manga/manga_list.html'
    context = {
        'manga_key': manga_value,
    }
    return render(request, html_name, context)

def mangaDetailView(request, id):
    manga_id = get_object_or_404(models.Manga_shops, id=id)
    html_name ='manga/manga_detail.html'
    context = {
        'manga_id': manga_id
    }
    return  render(request, html_name, context)