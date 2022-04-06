from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.myfunctioncall, name='indexs'),
    path('about/', views.myfunctionabout, name='about'),
    path('add/<int:a>/<int:b>', views.add, name='add'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
    path('index/', views.index, name='index'),
    path('second/', views.second, name='second'), 
    path('third/', views.third, name='third'),
    path('image_page/', views.image_page, name='image_page'),
    path('image_page2/', views.image_page2, name='image_page2'),
    path('image_page3/', views.image_page3, name='image_page3'),
    path('image_page4/', views.image_page4, name='image_page4'), 
    path('image_page5/<str:imagename>/', views.image_page5, name='image_page5'),
    path('myform/', views.myform, name='myform'),
    path('submitmyform/', views.submitmyform, name='submitmyform'),
    path('myform2/', views.myform2, name='myform2')
    


]