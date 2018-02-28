from django.contrib import admin
from .models import Category, Page, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    autocomplete_fields = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

# Register your models here.


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
