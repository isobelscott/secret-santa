from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    exclusions = models.ManyToManyField('Person', blank=True)
    def __str__(self):
        return f"{self.id}_{self.first_name}"

class Group(models.Model):
    persons = models.ManyToManyField('Person')
    is_current = models.BooleanField()

class Party(models.Model):
    gift_price_max = models.IntegerField()
    event_date = models.DateField()
    group_id = models.ForeignKey('Group', on_delete=models.PROTECT)
    organizer = models.IntegerField()

class Hat(models.Model):
    matches = models.JSONField()
    party_id = models.ForeignKey('Party', on_delete=models.PROTECT)
    group_id = models.ForeignKey('Group', on_delete=models.PROTECT)
    is_current = models.BooleanField()

class Wishlist(models.Model):
    person_id = models.ForeignKey('Person', on_delete=models.PROTECT)
    party = models.ForeignKey('Party', on_delete=models.PROTECT)


