from django.db import models

from category.models import Category


# Create your models here.


class Course(models.Model):
    ACTIVE = True
    INACTIVE = False
    STATUS_TYPE = [
        (ACTIVE, 'True'),
        (INACTIVE, 'False')
    ]
    name = models.CharField(max_length=42)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='%Y/%m/%d/img-course/', null=True, blank=True)
    video = models.FileField(upload_to='%Y/%m/%d/video-course/', null=True, blank=True)
    hit = models.BigIntegerField(default=0)
    price = models.BigIntegerField(default=0)
    status = models.BooleanField(choices=STATUS_TYPE, default=ACTIVE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    created_time = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f"{self.name}"


class Epizode(models.Model):
    ACTIVE = True
    INACTIVE = False
    STATUS_TYPE = [
        (ACTIVE, 'True'),
        (INACTIVE, 'False')
    ]
    name = models.CharField(max_length=42)
    lid = models.TextField(blank=True)
    number = models.BigIntegerField(default=0)
    status = models.BooleanField(choices=STATUS_TYPE, default=ACTIVE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="epizodes")
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Epizode'
        verbose_name_plural = 'Epizodes'

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_LESSON = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )

    FREE = True
    CASH = False

    STATUS_TYPE = (
        (FREE, 'free'),
        (CASH, 'cash'),
    )
    name = models.CharField(max_length=42)
    description = models.TextField(blank=True)
    status = models.BooleanField(choices=STATUS_LESSON, default=ACTIVE)
    epizode = models.ForeignKey(Epizode, on_delete=models.CASCADE, related_name="lessons")
    video = models.FileField(upload_to='%Y/%m/%d/video-lessons/', null=True, blank=True)
    voice = models.FileField(upload_to='%Y/%m/%d/voice/', null=True, blank=True)
    hit = models.BigIntegerField(default=0)
    is_free = models.BooleanField(choices=STATUS_TYPE, default=CASH)
    created_time = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return f"{self.name}"

