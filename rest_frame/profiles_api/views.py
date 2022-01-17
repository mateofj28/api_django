from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication                                                    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import serializer, models, permissions

# Create your views here.

#first apiView
class HelloApiView(APIView):
    ''' API VIEW TEST '''

    # get serializer created
    serializer_class = serializer.HelloSerializer 

    # functions http

    ''' METHOD GET HTTP '''
    def get(self, request, format=None):
        ''' return attribute of api view '''

        an_api_view = [
            'Using methods http as get, post, put, patch, delete',
            'Traditional Django similar view',
            'More control in logic',
            'manually mapped to urls'
        ]

        return Response({
            'message': 'Hello word!',
            'api_view': an_api_view
        })

    ''' METHOD POST HTTP '''
    def post(self, request):

        # request.data, the deposited data
        # new serializer
        serializer = self.serializer_class(data=request.data)

        ''' serializer has data ? '''
        if serializer.is_valid():
            ''' save data serializer name  '''
            name = serializer.validated_data.get('name')
            message = f'Hello {name}' # injection
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        ''' update an object '''
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        ''' partially update an object '''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        ''' delete an object '''
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    ''' API TEST VIEW SET '''

    serializer_class = serializer.HelloSerializer 

    def list(self, request):

        a_view_set = [
            'use methods (create, retrieve, update, destroy)', 
            'automatically map urls using routers',
            'more functionality, less code',
        ]

        return Response({
            'message' : 'Hello word!',
            'viewSet' : a_view_set
        })

    def post(self, request):        

        serializer = self.serializer_class(data=request.data)        

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ''' get a object and id '''
    def retrieve(self, request, pk=None):
        return Response({'method_http':'GET'})

    ''' update a object with id '''
    def update(self, request, pk=None):
        return Response({'method_http':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method_http':'PATCH'})        

    ''' delete a object with id '''
    def destroy(self, request, pk=None):
        return Response({'method_http':'DELETE'})


''' view set for serializeUserProfile '''
class UserProfileViewSet(viewsets.ModelViewSet):
    ''' create and update userProfile '''

    # define serialize
    serializer_class = serializer.UserProfilesSerializer    

    # list userProfile
    queryset = models.UserProfile.objects.all()

    # user authentication
    authentication_classes = (TokenAuthentication,)
    
    # user permissions
    permission_classes = (permissions.UpdateOwnProfile,)

    # add filter
    filter_backends = (filters.SearchFilter,)
    # filter field
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    ''' create user authentication tokens '''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES