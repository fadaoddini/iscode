import simplejson
from django.contrib import messages
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Category
from category.serializers import CategorySerializer
from learn import forms
from learn.forms import LessonForm
from mylogin.models import MyUser
from django.http import JsonResponse
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import cv2
import pyautogui

engine = pyttsx3.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


class CategoryApi(APIView):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, content_type='application/json; charset=UTF-8')


class TestView(View):
    template_name = 'web/index/voice.html'

    def get(self, request):
        context = dict()

        if request.user.is_anonymous:
            context['userinfo'] = None
        else:
            userinfo = MyUser.objects.filter(mobile=request.user.mobile).first()
            context['userinfo'] = userinfo
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request):
        context = dict()
        print("FORM DATA RECIVED")
        if "voiceman" not in request.FILES:
            messages.info(request, "فایل صوتی ارسال نشده است! ")
            return HttpResponseRedirect(reverse_lazy('test-voice'))
        file = request.FILES["voiceman"]
        print("fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiile")
        print(file)
        print("fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiile")
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                print("sayyyyyyyyyyyyyyyyyyyyyyyyy : \n")
                data = recognizer.record(source)
            try:
                texttest = recognizer.recognize_google(data, key=None, language="fa-IR")
                print(texttest)
                context['texttest'] = texttest
                return render(request, template_name=self.template_name, context=context,
                          content_type=None, status=None, using=None)
            except:
                messages.info(request, "کلا خطا اتفاق افتاد! ")
                return HttpResponseRedirect(reverse_lazy('test-voice'))
        else:
            messages.info(request, "کلا خطا اتفاق افتاد! ")
            return HttpResponseRedirect(reverse_lazy('test-voice'))


class AddLesson(View):
    template_name_lesson = 'web/lesson/index.html'
    template_name = 'web/lesson/add_lesson.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        form_lesson = LessonForm()
        context['form_lesson'] = form_lesson
        return render(request, template_name=self.template_name, context=context,
                        content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        context = dict()
        form = forms.LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.user = request.user
            lesson.save()
            messages.info(request, "درس با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return render(request, template_name=self.template_name_lesson, context=context,
                        content_type=None, status=None, using=None)


@csrf_exempt
def start_record(request):
    pk = request.POST.get('pk')
    name = request.user.first_name
    welcome(name)
    return JsonResponse({
        'msg': "text"
    })


@csrf_exempt
def stop_record(request):
    return JsonResponse({
        'msg': 'stop record'
    })


def test2(request):
    context = dict()
    name = request.user.first_name
    print(name)
    while True:
        take_command().lower()
        command = "test"
        print(command)
        if "bye" in command or "stop" in command:
            print(f"Goodbye {request.user.first_name} \n")
            speak("Goodbye" + request.user.first_name)
            break
    context['text'] = "dfdfd"
    return render(request, 'web/index/test.html', context=context)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def take_command():
    print("How can help you? \n")
    # speak("How can help you?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ... ")
        audio = r.listen(source)
        try:
            cm = r.recognize_google(audio, language="en-US")
            print(f"You said : {cm} \n")
            speak("Oh , yes very very very very good")

        except:
            print("Sorry, I didn't understand, please say again. \n")
            speak("Sorry, I didn't understand, please say again.")
            return "None"
        print("injaaaaaaaaaa")
        print(cm)
        print("injaaaaaaaaaa")
        return cm


def welcome(name):
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        text = "Hello " + name + ", Good Morning"
        speak(f"Hello {name}, Good Morning")
    elif 12 <= hour <= 18:
        print(f"Hello {name}, Good Afternoon. \n")
        text = "Hello" + name + ", Good Afternoon"
        speak(f"Hello {name}, Good Afternoon.")
    else:
        print(f"Hello {name}, Good Evening. \n")
        text = "Hello" + name + ", Good Evening"
        speak(f"Hello {name}, Good Evening.")

    print("lets start!")
    speak("lets start!")