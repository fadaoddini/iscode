from django.urls import path, include

from category.views import CategoryApi, TestView

urlpatterns = [
    path('category/', CategoryApi.as_view(), name='category-list'),

]
