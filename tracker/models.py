from django.db import models
from django.contrib.auth.models import User

class Drink(models.Model):
    name = models.CharField(max_length=100)
    caffeine_mg = models.IntegerField()
    sugar_g = models.IntegerField()
    volume_ml = models.IntegerField()

    def __str__(self):
        return self.name

class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.drink.name}"