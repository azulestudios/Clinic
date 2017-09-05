from django.conf.urls import url
from . import views as views

app_name = 'user'
urlpatterns = [
    url(r'^admin/', views.admin_home, name='home'),
]