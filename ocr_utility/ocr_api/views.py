from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from django.conf.urls import url


@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "POST":
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world! This is ocr_utility"})


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)


urlpatterns = [
    url(r"hello", hello_world),
    url(r"input_ocr", FileUploadView.as_view()),
]
