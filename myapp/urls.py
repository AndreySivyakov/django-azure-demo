from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home_page, name='myapp-home'),
    path('enter_new/', views.user_form2, name='myapp-new'),
    path('modify/', views.view_records, name='myapp-modify'),
    path('coming_soon/', views.blank_page, name='myapp-coming_soon'),
]
