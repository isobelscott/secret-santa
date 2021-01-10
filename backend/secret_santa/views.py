from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Person
from rest_framework import pagination, viewsets, filters
from .serializers import PersonSerializer

class CreatePerson(View):
    def post(self, request, *args, **kwargs):
        person = Person()
        person.first_name = request['first_name']
        person.email = request['email']
        person.exclusions = request['exclusions']
        person.save()

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_fields = ('id', 'exclusions')
