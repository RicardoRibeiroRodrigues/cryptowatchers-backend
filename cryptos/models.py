from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crypto(models.Model):
    crypto_id = models.CharField(max_length=200)
    buying_price = models.FloatField()
    quantity = models.FloatField()
    notes = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
