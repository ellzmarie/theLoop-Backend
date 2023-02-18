from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistsSerializer
from .models import Artist
from django.shortcuts import render, get_object_or_404

# Create your views here.

class Artist(APIView):
    
    def get(self, request):
        print(request)
        artist = Artist.objects.all()
        data = ArtistsSerializer(artist, many=True).data
        return Response(data)
    
    def post(self, request):
        print(request.data)
        artist = ArtistsSerializer(data=request.data)
        if artist.is_valid():
            artist.save()
            return Response(artist.data, status=status.HTTP_201_CREATED)
        else:
            return Response(artist.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetail(APIView):
    def get(self, request, pk):
        print(request)
        artist = get_object_or_404(Artist, pk=pk)
        data = ArtistsSerializer(artist).data
        return Response(data)
    
    def put(self, request, pk):
        print(request)
        artist = get_object_or_404(Artist, pk=pk)
        updated = ArtistsSerializer(artist, data=request.data, partial=True)
        if updated.is_valid():
            updated.save()
            return Response(updated.data)
        else:
            return Response(updated.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        print(request)
        artist = get_object_or_404(Artist, pk=pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)