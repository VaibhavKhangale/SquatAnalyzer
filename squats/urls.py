from django.urls import path
from .views import home, video_feed, stop_feed, squat_count_feed

urlpatterns = [
    path('', home, name='home'),
    path('video_feed/', video_feed, name='video_feed'),
    path('stop_feed/', stop_feed, name="stop_feed"),
    path('squat_count_feed/', squat_count_feed, name="squat_count_feed"),
]
