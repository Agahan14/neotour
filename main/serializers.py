import re

from rest_framework import serializers

from .models import Booking, Category, Review, Tour


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            "id",
            "image",
            "title",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "review",
            "nickname",
            "photo",
        ]


class TourDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = [
            "id",
            "title",
            "image",
            "description",
            "reviews",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "tour", "num_people", "phone_number", "additional_comments"]

    def validate_phone_number(self, value):
        pattern = r"^\+996\d{9}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                {
                    "error": "Invalid phone number. It should start with +996 and have 12 digits."
                }
            )

        return value
