from rest_framework import serializers
from .models import Person, Party, Group


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id', 'first_name', 'email', 'exclusions'
        )


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = (
            'id', 'party_name', 'gift_price_max', 'event_date', 'group_id', 'organizer'
        )

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id', 'persons', 'is_current'
        )
