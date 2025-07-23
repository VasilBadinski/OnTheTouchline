from django.db import models


class PlayerPositionChoices(models.TextChoices):
    GOALKEEPER = 'GK', 'Goalkeeper'
    DEFENDER = 'DF', 'Defender'
    MIDFIELDER = 'MF', 'Midfielder'
    ATTACKER = 'AT', 'Attacker'