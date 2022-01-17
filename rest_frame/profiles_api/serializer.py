from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ serialize a field for apiView """
    
    name = serializers.CharField(max_length=15)

''' serialize a model '''
class UserProfilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        ''' data to display '''
        fields = ('id', 'email', 'name', 'password')
        ''' settings '''
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style':{'input_type':'password'} #hide a password
            }
        }

        ''' function for creare new user '''
        def create(self, validated_data):
            ''' using the function created in the class UserProfileManager '''
            user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name = validated_data['name'],
                password = validated_data['password'],
            )

            return user

        def update(self, instance, validated_data):
            # the word is here ?
            if 'password' in validated_data:
                # to hash
                password = validated_data.pop('password')
                # change password normal to hash
                instance.set_password(password)

            # update the object
            return super().update(instance, validated_data)