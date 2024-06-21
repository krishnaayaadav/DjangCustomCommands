
from django.core.management import BaseCommand

from django.contrib.auth.models import User

class Command(BaseCommand):

    help =  'Use this command to generate users report'


    def handle(self, *args, **kwargs):

        all_users = User.objects.all()

        # your custom logic to regerate the users-reports
        user_report = list(all_users.values('id', 'username', 'is_active'))

        self.stdout.write(self.style.SUCCESS(f'\n User reports generated successfully\n reports: {user_report}'))