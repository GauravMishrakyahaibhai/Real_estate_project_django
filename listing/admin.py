from django.contrib import admin
from listing.models import Property
# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','description','address','price','bedrooms','bathrooms')
