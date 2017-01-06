from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from.models import auto_scraper,url
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import os,json,ast,csv

from django.core.exceptions import ObjectDoesNotExist




class UserApiView(APIView):

  permission_classes = (permissions.IsAuthenticated, )
  authentication_classes = (TokenAuthentication,)
  url_verify= URLValidator()

  def get(self, request, format=None):
      """
      Return a details of data scraped.
      """
      parameters = request.query_params.get('url', None)

      if parameters:
        try:
          sme_scraper_obj = auto_scraper.objects.get(url_id=parameters)


        except ObjectDoesNotExist:
          sme_scraper_obj = None

        if sme_scraper_obj:

          return Response(ast.literal_eval(sme_scraper_obj.data))
        else:
          #Check for valid url
          try:
             self.url_verify(parameters)
          except ValidationError,e:
             return  Response({'url_status':False})
          #status of result

          try:

             if  url.objects.get(url_link=parameters):
              return Response({'spider_status':'Running'})
          except:
            u = url(url_link=parameters)
            u.save()


            return Response({'spider_status':'Updated'})

  def post(self,request, *args, **kwargs):

      # url = request.data["url"]
      # data = request.data["data"]
      if request.data["url"] and request.data["data"]:

          sme = auto_scraper(url_id=request.data["url"],data= json.loads(request.data["data"]))
          sme.save()
          return Response({'data_status':True})
      else:

          return Response({'data_status':False})







