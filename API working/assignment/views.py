from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from assignment.models import UserInformation, ActivityPeriods
from assignment.serializers import UserSerializer, ActivitySerializer
# Create your views here.

class UserList(APIView):  
    '''
    This is an API class which is used to generate user information as well as their activities.
    '''
    def get(self, request):
        users = UserInformation.objects.all()
        serializer = UserSerializer(users, many = True)

        dictionary = {}    #To take in activity data from the model
        ls = []            #Storing start_time and end_time as tuples inside list
        actual_data = []   #Combining both the UserInformation model and ActivityPeriods model

        #This is to execute query for each user
        for i in range(len(serializer.data)):
            for j in ActivityPeriods.objects.filter(user_id=str(i + 1)):
                ls.append((j.start_time, j.end_time))   #Adding start_time and end_time in the form of tuples
            activity_list = []
            index = 0

            #Combining the two models
            for ik in range(len(ls)):
                activity_list.append({'start_time': ls[ik][0], 'end_time': ls[ik][0 + 1]})
                index += 1

            serializer.data[i]['activity_periods'] = activity_list
            actual_data.append(serializer.data[i])  
            activity_list = []
            ls = []
        #Conerting it into json format and sending it through API
        diction = {
            "ok": "True",
            "members": actual_data
        }
        return Response(diction)