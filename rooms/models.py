from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")


    """Model definition for room"""
    country = models.CharField(max_length=50, default="한국",)
    city = models.CharField(max_length=80, default="서울",)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    description = models.TextField()
    pet_friendly = models.CharField(max_length=20,)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices,)
    toilets = models.PositiveIntegerField()
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")
    category = models.ForeignKey("categories.Category",
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="rooms",
                                    blank=True,)
    # show string name and description
    def __str__(self):
        return self.name
    
    def total_amenities(self):
        return self.amenities.count()
    
    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "No reviews"
        else :
            total_rating = 0
            for review in room.reviews.all().values("rating"):
                total_rating += review.rating
            return round(total_rating / count, 2)
    
class Amenity(CommonModel):
    """Model definition for amenity"""
    name = models.CharField(max_length=80,)
    description = models.CharField(max_length=140, null=True, blank=True,)

    # show string name and description
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name_plural = "Amenities"
