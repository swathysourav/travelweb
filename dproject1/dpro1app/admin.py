from django.contrib import admin

# Register your models here.
from . models import travel
from . models import meetteam

admin.site.register(travel)
admin.site.register(meetteam)
