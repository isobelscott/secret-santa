from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Person, Party, Group
from rest_framework import pagination, viewsets, filters
from .serializers import PersonSerializer, PartySerializer, GroupSerializer


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


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    filter_fields = ('id', 'party_name', 'gift_price_max', 'event_date', 'group_id', 'organizer')


class IsGroupMemberFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only returns groups for which person is in group.
    """
    def filter_queryset(self, request, queryset, view):
        data = request.GET
        if data.get("person_id"):
            return queryset.filter(persons=data["person_id"])
        elif data.get("id"):
            return queryset.filter(id=data["id"])
        else:
            return queryset


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [IsGroupMemberFilterBackend]
    filter_fields = ('id', 'persons')
