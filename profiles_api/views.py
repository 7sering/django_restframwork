from rest_framework.views import APIView  # API VIEW
from rest_framework.response import Response  # For Response
from rest_framework.authentication import TokenAuthentication  # Token Authentication
from rest_framework import filters

from rest_framework import status

from profiles_api import serializers
from profiles_api import models
from profiles_api import permission

# API View
from rest_framework import viewsets


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


########################## ViewSet API #####################

class HelloViewSet(viewsets.ViewSet):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return YOUR_SERIALIZER_1
        elif self.request.method == 'GET':
            return YOUR_SERIALIZER_2
        else:
            return YOUR_DEFAULT_SERIALIZER

    def list(self, request):
        """Return Hello Message"""
        a_viewset = [
            'Use Actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle Update object by its ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

########################## Modal ViewSet API #####################


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle Creating and Updating Profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends =(filter.SearchFilter,)
    search_fields =('name', 'email', )
