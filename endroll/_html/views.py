from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.shortcuts import redirect

from django.views.generic.edit import FormView


from .models import Profile, Disc, Image, Movie, Suchedule
# from .forms import ReserveForm

# Create your views here.


def index(request):

    prof = get_object_or_404(Profile, id = 1)

    disc = get_list_or_404(Disc, show_at_home=True)

    move = get_list_or_404(Movie)

    suchedule = get_list_or_404(Suchedule, pickup=True)

    a = {
        'prof': prof,
        'suchedule': suchedule,

    }
    return render(request, 'index.html', a)

def schedule(request):
    schedule = get_list_or_404(Suchedule)
    d = {
      'sche': schedule,
    }
    return render(request, 'schedule.html', d)

def movie(request):
    return render(request, 'movie.html')

def disc(request):
    return render(request, 'discography.html')

def contact(request):
    return render(request, 'contact.html')
