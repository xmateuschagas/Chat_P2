from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include('carros.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticação do Django
    path('', lambda request: HttpResponseRedirect('/carros/')),
]
