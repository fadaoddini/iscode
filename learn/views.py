from django.shortcuts import render
from django.views import View

from mylogin.models import MyUser


class IndexView(View):
    template_name = 'web/index/index.html'

    def get(self, request):
        context = dict()
        if request.user.is_anonymous:
            context['userinfo'] = None
        else:
            userinfo = MyUser.objects.filter(mobile=request.user.mobile).first()
            context['userinfo'] = userinfo
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class CourseView(View):
    template_name = 'web/course/index.html'

    def get(self, request):
        context = dict()
        return render(request, template_name=self.template_name, context=context, content_type=None, status=None, using=None)


