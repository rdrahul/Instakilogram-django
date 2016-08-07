from django.contrib import admin
from models import Item, Photo

class photo_in_line(admin.StackedInline):
    model=Photo

class item_in_line(admin.ModelAdmin):
    inlines=[photo_in_line]

admin.site.register(Item,item_in_line)
admin.site.register(Photo)