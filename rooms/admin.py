from django.contrib import admin
from .models import Room, Amenity
# Register your models here to be shown in the admin panel.


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request):
    pass



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "price",
        "kind",
        "owner",
        "created_at",
        "rating",
        "total_amenities"
    )

    list_filter = (
        "country",
        "price",
        "rooms",
        "pet_friendly",
        "kind",
        "toilets",
        "owner",
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )