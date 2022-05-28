from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from entries.api.serializers import EntrySerializer
from entries.models import Entry

class EntryListApi(APIView):
    
    def get(self, request):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = EntrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    
class EntryDetailApi(APIView):
    
    def get(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        serializer = EntrySerializer(instance = entry)
        
        return Response(serializer.data)
    
    def put(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        serializer = EntrySerializer(instance = entry, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    def delete(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)