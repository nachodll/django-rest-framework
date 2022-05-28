from rest_framework import serializers
from entries.models import Entry


class EntrySerializer(serializers.Serializer):
    
    id = serializers.ReadOnlyField()
    datetime = serializers.DateTimeField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    
    def create (self, validated_data):
        instance = Entry(
            datetime = validated_data.get("datetime"),
            amount = validated_data.get("amount"),
            concept = validated_data.get("concept")
        )
        instance.save()
        
        return instance
    
    
    def update (self, instance, validated_data):
        instance.datetime = validated_data.get("datetime", instance.datetime)
        instance.concept = validated_data.get("concept", instance.concept)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.save()
        
        return instance