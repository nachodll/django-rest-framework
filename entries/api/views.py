from datetime import datetime
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
    
    
    def post(serf, request):
        
        serializer = EntrySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)