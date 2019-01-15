from django.urls import path
from .views import IndexPageView, DetailPageView, ResultPageView 

urlpatterns = [
    path('',IndexPageView.as_view(), name='index'),
    path('detail/',DetailPageView.as_view(), name='detail'),
    path('result/', ResultPageView.as_view(), name='result'),
]
