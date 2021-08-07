# Posts app module

from django.apps import AppConfig


class PostsConfig(AppConfig):
    # Post app settings
    default_auto_field = 'django.db.models.BigAutoField'

    name = 'posts'
    verbose_name = 'Posts'
