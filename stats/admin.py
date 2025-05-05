from django.contrib import admin

# Register your models here.
from .models import Player
from .models import GameStat
from .models import OpponentTeam


admin.site.register(Player)
admin.site.register(GameStat)
admin.site.register(OpponentTeam)