from rest_framework.views import APIView #API VIEW 
from rest_framework.response import Response #For Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Retrun a list of API View Features"""
        an_apiview = [
            "Use HTTP methods as function(get, post,patch, put, delete)",
            "Is similar to a traditional Django View ",
            "Gives you the  most control over your application logic ",
            "Is mapped manually to URLs ",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
