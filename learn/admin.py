from django.contrib import admin
from django.contrib.admin import register

from learn.models import Course, Epizode, Lesson


# Register your models here.

@register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')
    search_fields = ('name', 'category')
    list_editable = ('status',)
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            course = Course.objects.filter(pk=queryone.pk).first()
            course.status = True
            course.save()

    def deactive_all(self, request, queryset):
        for queryone in queryset:
            course = Course.objects.filter(pk=queryone.pk).first()
            course.status = False
            course.save()


@register(Epizode)
class EpizodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'status')
    search_fields = ('name', 'course')
    list_editable = ('status',)
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            epizode = Epizode.objects.filter(pk=queryone.pk).first()
            epizode.status = True
            epizode.save()

    def deactive_all(self, request, queryset):
        for queryone in queryset:
            epizode = Epizode.objects.filter(pk=queryone.pk).first()
            epizode.status = False
            epizode.save()


@register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'epizode', 'video', 'voice', 'hit', 'is_free', 'status')
    search_fields = ('name', 'epizode')
    list_editable = ('status',)
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            lesson = Lesson.objects.filter(pk=queryone.pk).first()
            lesson.status = True
            lesson.save()

    def deactive_all(self, request, queryset):
        for queryone in queryset:
            lesson = Lesson.objects.filter(pk=queryone.pk).first()
            lesson.status = False
            lesson.save()



