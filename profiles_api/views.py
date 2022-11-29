from rest_framework.views import APIView  # API VIEW
from rest_framework.response import Response  # For Response

from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
           return YOUR_SERIALIZER_1
        elif self.request.method == 'GET':
           return YOUR_SERIALIZER_2
        else:
            return YOUR_DEFAULT_SERIALIZER



    def get(self, request, format=None):
        """Retrun a list of API View Features"""
        an_apiview = [
            "Use HTTP methods as function(get, post,patch, put, delete)",
            "Is similar to a traditional Django View ",
            "Gives you the  most control over your application logic ",
            "Is mapped manually to URLs ",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    

    def post(self, request):
        """Create a hello message with our name"""
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating of an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete Object"""
        return Response({'method': 'DELETE'})