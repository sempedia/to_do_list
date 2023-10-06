# TO_DO_APP/td_env/To_Do_List/clearcache.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Clears the cache'

    def handle(self, *args, **kwargs):
        # Your code to clear the cache goes here
        self.stdout.write(self.style.SUCCESS('Cache cleared successfully'))
