from django.db import models
from django.contrib.auth.models import User
USER_TYPE = (('DOCTOR', 'DOCTOR'), ('RECEPTIONIST', 'RECEPTIONIST'), ('PATIENT', 'PATIENT'),)
USER_SPECIALISED = (('EMPLANT', 'EMPLANT'), ('ORTHO', 'ORTHO'))
USER_GENDER = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'),)
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=15, choices=USER_TYPE, default='PATIENT')
	user_addr = models.CharField(max_length=155, null=True )
	user_mobile = models.IntegerField(null=True )
	#user_hire_date = models.
	#user_end_date = models.
	#user_dob = models.
	user_specialised = models.CharField(max_length=15, choices=USER_SPECIALISED, default='EMPLANT')
	user_sex = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
