from django.contrib import admin

from .models import Movie, ExtraInfo, Review, Aktor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ("name", "description")
    list_display = ("name", "description")
    list_filter = ("name", "description")
    search_fields = ("name", "description")

admin.site.register(ExtraInfo)

admin.site.register(Review)

admin.site.register(Aktor)
