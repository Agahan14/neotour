from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response

from .filters import TourFilter
from .models import Booking, Category, Review, Tour
from .pagination import CustomPagination
from .serializers import (
    BookingSerializer,
    CategorySerializer,
    ReviewSerializer,
    TourDetailSerializer,
    TourListSerializer,
)


class TourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = TourFilter
    serializer_class = TourListSerializer


class TourDetailAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class RecommendTourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.exclude(season__isnull=True).order_by("season")
    serializer_class = TourListSerializer


# class TourCategoryListAPIView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class TourDetailAPIView(generics.RetrieveAPIView):
#     queryset = Tour.objects.all()
#     serializer_class = TourSerializer

# class ReviewListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class BookingCreateAPIView(generics.CreateAPIView):
#     serializer_class = BookingSerializer

#     def create(self, request, *args, **kwargs):
#         request.data['phone_number'] = '+996' + request.data.get('phone_number', '')

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
