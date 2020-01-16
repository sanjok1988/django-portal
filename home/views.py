from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request,template_name='index.html')
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'