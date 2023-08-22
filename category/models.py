from django.db import models

# Create your models here.


class Category(models.Model):
    ACTIVE = True
    INACTIVE = False
    STATUS_TYPE = (
        (ACTIVE, 'True'),
        (INACTIVE, 'False')
    )
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    status = models.BooleanField(choices=STATUS_TYPE, default=ACTIVE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name