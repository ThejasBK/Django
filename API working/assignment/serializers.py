from rest_framework import serializers
from assignment.models import UserInformation, ActivityPeriods

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserInformation
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta():
        model = ActivityPeriods
        fields = '__all__'