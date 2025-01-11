from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):
    """Category Model Definitions."""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=80)
    kind = models.CharField(
        max_length=20,
        choices = CategoryKindChoices.choices,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
