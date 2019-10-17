from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


class photoInline(admin.StackedInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (photoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country",
                        "city", "address", "price", "room_type",)}
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book",)}
        ),
        (
            "More About the Space",
            {
                # "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules")
            }
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths",)}
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("^city", "^host__username",)

    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "get_thumbnail",
    )
