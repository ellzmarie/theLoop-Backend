from django.urls import path
from .views import Artist, ArtistDetail

urlpatterns = [
    path('', Artist.as_view(), name='artist'),
    path('<int:pk>', ArtistDetail.as_view(), name='Artist_detail')
]