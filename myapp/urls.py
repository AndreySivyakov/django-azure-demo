from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    #path('', views.user_form1, name='myapp-home'),
    path('', views.user_form2, name='myapp-home'),
    path('modify/', views.view_records, name='myapp-modify'),
    path('coming_soon/', views.blank_page, name='myapp-coming_soon'),
]
