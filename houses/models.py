from django.db import models

# Create your models here.
class House(models.Model):

    """Model definition for house"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(default=True, 
                                      help_text="Is pet allowed in the house?",
                                      verbose_name="Pet Allowed")
    
    #what happend when the reference is deleted
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


