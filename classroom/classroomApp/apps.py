from django.apps import AppConfig


class ClassroomAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classroomApp'

    def ready(self):
        import classroomApp.signals
