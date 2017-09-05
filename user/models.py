from django.db import models
from django.contrib.auth.models import User
USER_TYPE = (('DOCTOR', 'DOCTOR'), ('RECEPTIONIST', 'RECEPTIONIST'), ('PATIENT', 'PATIENT'),)
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=15, choices=USER_TYPE, default='PATIENT')
	user_addr = models.CharField(max_length=155, null=True )
