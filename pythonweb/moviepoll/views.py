from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index_page.html'

class DetailPageView(TemplateView):
    template_name = 'detail_page.html'

class ResultPageView(TemplateView):
    template_name = 'result_page.html'
    


