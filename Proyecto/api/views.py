# from ast import arg
# from multiprocessing import context
# from urllib import response
# from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .serializer import *
from .models import Postulants, StateChange
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

class PostulantsViewSet(APIView):
 
  def get(self, request, format=None):
      post = Postulants.objects.all()
      serializer = PostulantsSerializer(post,many=True)
      return Response(serializer.data)
  
  def post(self, request, format=None):
        #print(self.response.content)
        serializer = PostulantsSerializerSave(data=request.data)
        # print(serializer)
        # print(serializer.is_valid())
        if serializer.is_valid():
            save = serializer.save()
            print(save)
            #cuerpo =Postulants.objects.get(Id=10123)
            # print(cuerpo)
            StateChange.objects.create(Id_Postulants=save, 
                                        State_Change='Sin Definir', 
                                        Date_Change=str(save.Date_Modificate), 
                                        Description='New into Postulant'
                                        )   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostulantDetail(APIView):
    def get_object(self, Id):
        try:
            return Postulants.objects.get(Id=Id)
        except Postulants.DoesNotExist:
            raise Http404

    def get(self, request,Id, format=None):
        post = self.get_object(Id)  
        serializer = PostulantsSerializer(post)
        return Response(serializer.data)

    def put(self, request,Id, format=None):
        post = self.get_object(Id)
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        dateNow = datetime.datetime.now()
        post.Date_Registration = date
        post.Date_Modificate = dateNow
        serializer = PostulantsSerializerModify(instance=post, data=request.data)
        # print(serializer)
        # print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,Id, format=None):
        print("01")
        post = self.get_object(Id)
        print("02")
        serializer = PostulantsSerializerModifyState(instance=post, data=request.data)
        print("03")
        print(serializer)
        print("04")
        #print(serializer.Id)
        print("05")
        print(serializer.is_valid())
        print("06")
        if serializer.is_valid():
            save = serializer.save()
            print(save.Actual_State)
            StateChange.objects.create(Id_Postulants=save, 
                                        State_Change=str(save.Actual_State),  
                                        Description=str(save.Reason)
                                        )   
            print("08")
            return Response(status=status.HTTP_204_NO_CONTENT)      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Id, format=None):
        post = self.get_object(Id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)