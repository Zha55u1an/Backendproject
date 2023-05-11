from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('post/create/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('theme/select/', views.select_theme, name='select_theme'),
    path('theme/customize/int:theme_id/', views.customize_theme, name='customize_theme'),
    path('post/<int:pk>/comments/', views.post_comments, name='post_comments'),
    path('', views.post_list, name='post_list'),
    path('', views.home_page, name='home_page'),
    path('', views.login,name='login')
]