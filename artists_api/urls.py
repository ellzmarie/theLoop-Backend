from django.urls import path
from .views import Artists, ArtistsDetail

urlpatterns = [
    path('', Artists.as_view(), name='artists'),
    path('<int:pk>', ArtistsDetail.as_view(), name='Artists_detail')
]