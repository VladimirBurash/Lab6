from django.shortcuts import render
from django.views import View

from lab6.models import Artist


# Create your views here.
def main(request):
    artists = Artist.objects.all()

    return render(request, 'main.html', {'artist': artists} )
