from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""

        an_api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to the traditional Django View',
            'Gives you the most control of your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})

    def post(self, request):
        """Create a hello message with our name"""

        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializers.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating the object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handle partial update of the object"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_view_set = [
            'Uses actions''(get, post, patch, put, delete)',
            'ya 123'
        ]
        return Response({'message': 'Hello', 'a_view': a_view_set})

    def create(self, request):
        """Create new hello message"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializers.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retreive(self, request, pk=None):
        """Handle getting an object by ID"""

        return Response({'method': 'get'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'put'})

    def partial_update(self, request, pk=None):
        """Handle updating part an object"""

        return Response({'method': 'patch'})

    def destroy(self, request, pk=None):
        """Handle destroing the object"""

        return Response({'method': 'delete'})
