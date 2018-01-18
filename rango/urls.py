from django.urls import path, re_path

from . import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    re_path(r'^category/(?P<category_name_slug>[\w-]+)/$', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    re_path('(?P<category_name_slug>[\w-]+)/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
]
