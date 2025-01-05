from django.db import models

# Create your models here.

class CommonModel(models.Model):
    """Common Model definition"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # django will not automatically put this model in the database
    class Meta:
        abstract = True
