from django.db import models
from common.models import CommonModel

# Create your models here.
class Booking(CommonModel):
    
    class BookingKindCoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(max_length=20, 
                            choices=BookingKindCoices.choices,)
    user = models.ForeignKey("users.User", 
                             on_delete=models.CASCADE,)
    room = models.ForeignKey("rooms.Room", 
                             on_delete=models.SET_NULL,
                              null=True, 
                              blank=True)
    experience = models.ForeignKey("experiences.Experience", 
                                   on_delete=models.SET_NULL,
                                    null=True, 
                                    blank=True)
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"