from rest_framework import serializers
from entries.models import Entry


class EntrySerializer(serializers.Serializer):
    
    id = serializers.ReadOnlyField()
    datetime = serializers.DateTimeField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    
    def create (self, validated_data):
        instance = Entry()
        instance.datetime = validated_data.get("datetime")
        instance.amount = validated_data.get("amount")
        instance.concept = validated_data.get("concept")
        
        return instance
    
    
    def update (self, instance, validatad_data):
        pass
        