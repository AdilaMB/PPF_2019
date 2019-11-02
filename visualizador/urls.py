"""visualizador URL Configuration

The `urlpatterns` list routes URLs to view_aux. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function view_aux
    1. Add an import:  from my_app import view_aux
    2. Add a URL to urlpatterns:  path('', view_aux.home, name='home')
Class-based view_aux
    1. Add an import:  from other_app.view_aux import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('appdigilib.url')),

]
