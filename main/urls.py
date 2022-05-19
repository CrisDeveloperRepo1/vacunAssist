from django.urls import path, include
from . import views
app_name= 'main'

urlpatterns = [
    path('', views.homepage,name= 'homepage'),
    path('registro/', views.registro , name="registro"),
    path('', views.login, name= 'login' )
]
