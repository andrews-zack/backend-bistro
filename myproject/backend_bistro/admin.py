from django.contrib import admin
from .models import MenuItem, Cuisine, Category

class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(MenuItem, MenuAdmin)

class CuisineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cuisine, CuisineAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
