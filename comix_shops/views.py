from django.shortcuts import render, get_object_or_404
from . import models

def mangaListView(request):
    manga_value = models.Manga_shops,object.all()
    html_name = 'comix/comix_list.html'
    context = {
        'comix_key': manga_value,
    }
    return render(request, html_name, context)

def mangaDetailView(request, id):
    manga_id = get_object_or_404(models.Manga_shops, id=id)
    html_name ='comix/comix_detail.html'
    context = {
        'comix_id': manga_id
    }
    return  render(request, html_name, context)