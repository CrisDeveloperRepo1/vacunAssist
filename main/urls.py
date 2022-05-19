from django.urls import path, include
from . import views
app_name= 'main'

urlpatterns = [
    path('', views.homepage,name= 'homepage'),
<<<<<<< HEAD

    path('registro/', views.registro , name="registro"),



    path('login', views.login, name= 'login' ),

=======
    path('registro/', views.registro , name="registro"),
    path('login/', views.login, name= 'login' )
>>>>>>> 4c66fe36671eada1fef6ffc459bc217a227199a5
]
