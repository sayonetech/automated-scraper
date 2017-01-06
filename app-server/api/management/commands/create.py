from django.core.management import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import os

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Automaticaly create a Super user"

    # def add_arguments(self, parser):
    #     parser.add_argument('username')
    #     parser.add_argument('password')
    #     parser.add_argument('email')


    # A command must define handle()
    def handle(self, *args, **options):

      # name = options['username']
      # psw = options['password']
      # mail=options['email']
      name=os.environ['SUPER_USERNAME']
      psw=os.environ['SUPER_PASSWORD']
      mail=os.environ['SUPER_EMAIL']


      try:
          user = User.objects.create_superuser(username=name, email=mail,password=psw)
          user.save()

      except:
          pass