from django.contrib import admin
from django.urls import include, path

from core.views import home,teste

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    path('', home, name='home'), 
    path('teste/', teste, name='teste'), 

    path('', include('gcms.urls')),
    
]
