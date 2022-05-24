from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'
