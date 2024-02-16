from datetime import tzinfo
from time import timezone
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Postulants(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    First_Name = models.CharField(db_column='First_Name', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    Second_Name = models.CharField(db_column='Second_Name', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    Age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    Profession = models.CharField(db_column='Profession', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    Actual_State = models.CharField(db_column='Actual_State', max_length=12, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    Date_Registration = models.DateField(db_column='Date_Registration',auto_now_add=True)  # Field name made lowercase.
    Date_Modificate = models.DateTimeField(db_column='Date_Modificate',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Postulants'

class StateChange(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Id_Postulants = models.ForeignKey(Postulants, models.DO_NOTHING, db_column='Id_Postulants')  # Field name made lowercase. ,on_delete=models.CASCADE
    State_Change = models.CharField(db_column='State_Change', max_length=12, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    Date_Change = models.DateTimeField(db_column='Date_Change',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    Description = models.CharField(db_column='Description', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'State_Change'