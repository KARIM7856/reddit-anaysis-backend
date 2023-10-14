from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.hot_topics),
    path('hashtags', views.HashTag.as_view()),
    path('testlist', views.TestList.as_view()),
]