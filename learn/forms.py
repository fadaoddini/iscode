from django import forms

from learn.models import Course, Epizode, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'image', 'category', 'price']


class EpizodeForm(forms.ModelForm):
    class Meta:
        model = Epizode
        fields = ['name', 'course']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'epizode', 'voice']