from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.webtoon_list, name='webtoon-list'),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('<int:pk>/', views.episode_detail, name='episode-detail'),
]