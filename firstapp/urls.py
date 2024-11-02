from django.urls import path
from firstapp.views import HomePageView, CourseView
urlpatterns= [
    path('', HomePageView.as_view(), name='home'),
    path("courses/", CourseView.as_view(), name = 'courses'),
]