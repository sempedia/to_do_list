# TO_DO_APP/td_env/To_Do_List/To_Do_List/apps.py
from django.apps import AppConfig

class ToDoListConfig(AppConfig):
    name = 'To_Do_List'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import To_Do_List.clearcache  # Make sure the import statement is correct

