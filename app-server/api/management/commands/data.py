from django.core.management import BaseCommand
from ...models import url
import csv

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

     if url.objects.all():
         url.objects.all().delete()
     with open('/app/urls.csv') as f:
       reader = csv.reader(f, delimiter=',')
       links=list(reader)
     for link in links:
       
       u=url(url_link=link[0],status=0)
       u.save()