from rest_framework import permissions

''' custom permissions '''
class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permissions(self, request, view, obj):
        ''' user tries update your information or has permissions ? '''
        if request.method in permissions.SAFE_METHODS:
            # not the original user, read only            
            return False 

        ''' if true, is original user '''
        return obj.id == request.user.id