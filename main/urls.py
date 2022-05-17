from django.urls import path, include
from . import views
app_name= 'main'

urlpatterns = [
    path('', views.homepage,name= 'homepage'),
<<<<<<< HEAD
    path('registro/', views.registro , name="registro")

=======
    path('', views.login, name= 'login' )
>>>>>>> 8a1dbd2616431fc6a980c63c0c611e31898e16e5
]
