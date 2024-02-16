
from email.policy import default
from multiprocessing.sharedctypes import Value
from sre_parse import State
from .models import Postulants, StateChange
from rest_framework import serializers
from django.http import Http404
import datetime

class PostulantsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Postulants
    #exclude = ['is_removed', 'created', 'modified']
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    # exclude = ['is_removed', 'created', 'modified']
    fields = '__all__'

class PostulantsSerializerModify(serializers.ModelSerializer):
  class Meta:
    model = Postulants
    #exclude = ['is_removed', 'created', 'modified']
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    # exclude = ['is_removed', 'created', 'modified']
    fields = ["Name","First_Name","Second_Name","Age","Profession","Date_Modificate"]

class PostulantsSerializerModifyState(serializers.ModelSerializer):
  State = serializers.CharField(max_length=12)
  Actual_State = State 
  Reason = serializers.CharField(max_length=100,allow_blank =True)
  class Meta:
    model = Postulants
    #exclude = ['is_removed', 'created', 'modified']
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    # exclude = ['is_removed', 'created', 'modified']
    fields = ["Actual_State","State","Reason"]

class PostulantsSerializerSave(serializers.ModelSerializer):
  #dateNow = datetime.datetime.now(pytz.timezone('US/Central') )
  # date = datetime.datetime.now().strftime('%Y-%m-%d')
  # dateNow = datetime.datetime.now()
  # Date_Registration = serializers.DateField(auto_now_add=True)
  # Date_Modificate = serializers.DateTimeField(auto_now_add=True)
  Actual_State = serializers.CharField(max_length=12,default ='Sin Definir')
  #print(str(dateNow))

  class Meta:
    model = Postulants
    #exclude = ['is_removed', 'created', 'modified']
    fields = ["Id","Name","First_Name","Second_Name","Age","Profession","Actual_State","Date_Registration","Date_Modificate"]
    #fields = '__all__'

  

# class StateSerializerSave(serializers.ModelSerializer):
#   dateNow = datetime.datetime.now()
#   date = datetime.datetime.now().strftime('%Y-%m-%d')

#   #Id_Postulants = serializers.IntegerField(Postulants.Id)
#   State_Change = serializers.CharField(max_length=12,default ='Sin Definir')  # Field name made lowercase.
#   Date_Change = serializers.DateTimeField(default=str(dateNow))  # Field name made lowercase.
#   Description = serializers.CharField(max_length=100,default='New into Postulant')

#   class Meta:
#     model = StateChange
#     #exclude = ['is_removed', 'created', 'modified']
#     fields = ["Id_Postulants","State_Change","Date_Change","Description"]
#     #fields = '__all__'

# class PostulantsSerializerSave(serializers.ModelSerializer):
  

#   Date_Registration = serializers.SerializerMethodField()
#   Date_Modificate = serializers.SerializerMethodField()

#   def validate(self,data):
#         #other wise you can set default value of age here,
#       dateNow = datetime.datetime.now()
#       date = "%s/%s/%s" % (dateNow.year, dateNow.month,dateNow.day) 
#       if data.get('Date_Registration',None)==None: #this conditon will be true only when age = serializer.IntergerField(required=False)
#           data['Date_Registration']=date
#           data['Date_Modificate']=dateNow
#       return data


#   class Meta:
#     model = Postulants
#     #exclude = ['is_removed', 'created', 'modified']
#     fields = ["Name","First_Name","Second_Name","Age","Profession","Actual_State","Date_Registration","Date_Modificate"]
#     #fields = '__all__'






# class PostulantsSerializerSave(serializers.Serializer):
#   dateNow = datetime.datetime.now()
#   date = "%s/%s/%s" % (dateNow.year, dateNow.month,dateNow.day) 

#   Name = serializers.CharField(max_length=50)  # Field name made lowercase.
#   First_Name = serializers.CharField(max_length=50)  # Field name made lowercase.
#   Second_Name = serializers.CharField(max_length=50)  # Field name made lowercase.
#   Age = serializers.IntegerField()  # Field name made lowercase.
#   Profession = serializers.CharField(max_length=50)  # Field name made lowercase.
#   Actual_State = serializers.CharField(max_length=12)  # Field name made lowercase.
#   Date_Registration = serializers.DateField(default =date )  # Field name made lowercase.
#   Date_Modificate = serializers.DateTimeField(default=dateNow)

#   def validate_Name(self,value):
#     print(value)
#     pass

#   def validate_First_Name(self,value):
#     print(value)
#     pass

#   def validate_Second_Name(self,value):
#     print(value)
#     pass

#   def validate_Age(self,value):
#     print(value)
#     pass

#   def validate_Profession(self,value):
#     print(value)
#     pass

#   def validate_Actual_State(self,value):
#     print(value)
#     pass

#   def validate_Date_Registration(self,value):
#     print(value)
#     pass

#   def validate_Date_Modificate(self,value):
#     print(value)
#     pass

