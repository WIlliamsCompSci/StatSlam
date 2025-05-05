from django.shortcuts import render
from .models import Player
from .models import OpponentTeam
from .models import GameStat


# Create your views here.
def index(request):
    obj=Player.objects.all()
    context={
        "obj":obj,
    }
    return render(request,"dashboard.html", context)

def masterstats(request):
    obj=Player.objects.all()
    context={
        "obj":obj,
    }
    return render(request,"masterstats.html", context)

def searchplayer(request):
    return render(request, "searchplayer.html")