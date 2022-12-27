from django.http import HTTPResponse
import datetime
def Current_datetime(request):
  now=datetime.datetime.now()
  html="It is now %s/body/html% now"
  return HTTPResponse(html)