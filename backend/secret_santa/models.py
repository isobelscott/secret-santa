from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    exclusions = models.JSONField()

class Group(models.Model):
    group = models.JSONField()

class Party(models.Model):
    gift_price_max = models.IntegerField()
    event_date = models.DateField()
    group_id = models.ForeignKey('Group')
    organizer = models.IntegerField()

class Hat(models.Model):
    matches = models.JSONField()
    party_id = models.ForeignKey('Party')
    group_id = models.ForeignKey('Group')
    is_current = models.BooleanField()

class Wishlist(models.Model):
    person_id = models.ForeignKey('Person')
    party = models.ForeignKey('Party')


