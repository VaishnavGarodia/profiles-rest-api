from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


# Create your views here.

class APIView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        api_view = ["1","2","3","4"]

        return Response({"message":"hello", "api_view":api_view})

    def post(self, request):
        """Post your name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({"method":"put"})
    def patch(self, request):
        """Handles a partial update of an object"""
        return Response({"method":"patch"})
    def delete(self, request):
        """Delete an Object"""
        return Response({"method":"delete"})
                
