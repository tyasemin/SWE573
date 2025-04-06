from django.db import models
import pycountry

COUNTRY_CHOICES = [(country.name, country.name) for country in pycountry.countries]

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    profession = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.username
