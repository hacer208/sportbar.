from django.contrib import admin
from .models import Category,Products,Basket

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products)
admin.site.register(Basket)