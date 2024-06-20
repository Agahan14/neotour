from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField()
    place = models.CharField(max_length=100)
    season = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    nickname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)

    def __str__(self):
        return f"Review for {self.tour.title} by {self.nickname}"


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    num_people = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    additional_comments = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.tour.title}"
