from django.contrib import admin
from django.contrib.admin import register

from category.models import Category


# Register your models here.

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'status')
    search_fields = ('name',)
    list_editable = ('status',)
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            category = Category.objects.filter(pk=queryone.pk).first()
            category.status = True
            category.save()

    def deactive_all(self, request, queryset):
        for queryone in queryset:
            category = Category.objects.filter(pk=queryone.pk).first()
            category.status = False
            category.save()
