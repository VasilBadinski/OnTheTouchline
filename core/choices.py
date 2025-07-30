from django.db import models


class PlayerPositionChoices(models.TextChoices):
    GOALKEEPER = 'GK', 'Вратар'
    DEFENDER = 'DF', 'Защитник'
    MIDFIELDER = 'MF', 'Халф'
    ATTACKER = 'AT', 'Нападател'