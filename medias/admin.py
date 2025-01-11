from django.contrib import admin

# Register your models here.
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "name",
        "description",
        "file",
    )
    list_filter = ("kind",)