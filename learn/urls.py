from django.urls import path, include

from learn.views import CourseView

urlpatterns = [
    path('index/', CourseView.as_view(), name='course-index'),
]
