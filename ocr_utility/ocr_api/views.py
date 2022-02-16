from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls import url, include

@api_view(['GET', 'POST'])
def hello_world(request):
        if request.method == 'POST':
                return Response({"message": "Got some data!", "data": request.data})
        return Response({"message": "Hello, world!"})

urlpatterns = [
  url(r'hello', hello_world),
]