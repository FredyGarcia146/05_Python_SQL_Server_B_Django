from django.db import models

# Create your models here.
class Postulants(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_Name', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    actual_state = models.CharField(db_column='Actual_State', max_length=12, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    date_registration = models.DateField(db_column='Date_Registration')  # Field name made lowercase.
    date_modificate = models.DateTimeField(db_column='Date_Modificate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Postulants'


class StateChange(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_postulants = models.ForeignKey(Postulants, models.DO_NOTHING, db_column='Id_Postulants')  # Field name made lowercase. ,on_delete=models.CASCADE
    state_change = models.CharField(db_column='State_Change', max_length=12, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    date_change = models.DateTimeField(db_column='Date_Change', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'State_Change'