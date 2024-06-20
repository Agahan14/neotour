from django.urls import path
from . import views

urlpatterns = [
    # path('discovery/', views.DiscoveryTourListAPIView.as_view(), name='discovery-tour-list'),
    # path('recommend/', views.RecommendTourListAPIView.as_view(), name='recommend-tour-list'),
    # path('categories/', views.TourCategoryListAPIView.as_view(), name='tour-category-list'),
    # path('tours/<int:pk>/', views.TourDetailAPIView.as_view(), name='tour-detail'),
    # path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    # path('bookings/create/', views.BookingCreateAPIView.as_view(), name='booking-create'),
    path('tours-list/', views.TourListAPIView.as_view(), name='tour-list'),
    path('tour-detail/<int:pk>/', views.TourDetailAPIView.as_view(), name='tour-detail'),
    path('booking-create/', views.BookingCreateAPIView.as_view(), name='booking-create'),
    path('recommend-tours/', views.RecommendTourListAPIView.as_view(), name='recommend-tour-list'),
]   
