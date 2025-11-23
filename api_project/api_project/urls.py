from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django project is working!")

urlpatterns = [
    path('', home),  # Root URL for sanity check
    path('admin/', admin.site.urls),
     path('api/', include('api.urls')),
     path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]

