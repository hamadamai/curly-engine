from django.conf.urls import url
from django.urls import path
from polls import views

urlpatterns = [
    path('polls_first/', views.detailfirst),
    path('polls0/', views.detail0, name='polls0'),
    path('polls1/', views.detail1, name='polls1'),
    path('polls2/', views.detail2, name='polls2'),
    path('polls3/', views.detail3, name='polls3'),
    path('polls4/', views.detail4, name='polls4'),
    path('polls20/', views.detail20, name='polls20'),
    path('polls30/', views.detail30, name='polls30'),
    path('polls100/', views.detaillast, name='polls100'),

]
