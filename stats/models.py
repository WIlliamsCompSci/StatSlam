from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class OpponentTeam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GameStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_stats')
    opponent = models.ForeignKey(OpponentTeam, on_delete=models.CASCADE, related_name='game_stats')
    
    fg_made = models.PositiveIntegerField(default=0)
    fg_attempted = models.PositiveIntegerField(default=0)
    
    three_pt_made = models.PositiveIntegerField(default=0)
    three_pt_attempted = models.PositiveIntegerField(default=0)
    
    ft_made = models.PositiveIntegerField(default=0)
    ft_attempted = models.PositiveIntegerField(default=0)

    oreb = models.PositiveIntegerField(default=0)
    dreb = models.PositiveIntegerField(default=0)

    ast = models.PositiveIntegerField(default=0)
    stl = models.PositiveIntegerField(default=0)
    blk = models.PositiveIntegerField(default=0)
    to = models.PositiveIntegerField(default=0)
    pf = models.PositiveIntegerField(default=0)

    @property
    def reb(self):
        return self.oreb + self.dreb

    @property
    def fg_pct(self):
        return round((self.fgm / self.fga) * 100, 2) if self.fga else 0

    @property
    def ft_pct(self):
        return round((self.ftm / self.fta) * 100, 2) if self.fta else 0

    @property
    def three_pct(self):
        return round((self.three_pm / self.three_pa) * 100, 2) if self.three_pa else 0