from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def admin_home(request):
	user = User.objects.get(id=1)
	return render(request, 'AdminLTE-2.3.0/index.html', { 'user':user })