from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistsSerializer
from .models import Artist
from django.shortcuts import render, get_object_or_404

# Create your views here.

class Artists(APIView):
    
    def get(self, request):
        print(request)
        artists = Artist.objects.all()
        data = ArtistsSerializer(artists, many=True).data
        return Response(data)
    
    def post(self, request):
        print(request.data)
        artists = ArtistsSerializer(data=request.data)
        if artists.is_valid():
            artists.save()
            return Response(artists.data, status=status.HTTP_201_CREATED)
        else:
            return Response(artists.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistsDetail(APIView):
    def get(self, request, pk):
        print(request)
        artists = get_object_or_404(Artist, pk=pk)
        data = ArtistsSerializer(artists).data
        return Response(data)
    
    def put(self, request, pk):
        print(request)
        artists = get_object_or_404(Artist, pk=pk)
        updated = ArtistsSerializer(artists, data=request.data, partial=True)
        if updated.is_valid():
            updated.save()
            return Response(updated.data)
        else:
            return Response(updated.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        print(request)
        artists = get_object_or_404(Artist, pk=pk)
        artists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)