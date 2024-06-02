import modeltranslation
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Good)
admin.site.register(Comment)


@admin.register(Movie)
class MovieAdmin(modeltranslation.admin.TranslationAdmin):
    list_display = ("title",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
