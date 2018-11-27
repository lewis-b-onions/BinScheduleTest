"""notable_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.resources import NoteResource, BinScheduleResource
from tastypieapp.api import EntryResource
from django.conf.urls import url, include

note_resource = NoteResource()
binschedule_resource= BinScheduleResource()
entry_resource = EntryResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
  #  url(r'^api/', include(note_resource.urls)),
    url(r'^binschedule/', include(binschedule_resource.urls)),
    url(r'^blog/', include('tastypieapp.urls')),
    url(r'^api/', include(entry_resource.urls))
]

# After instantiating the NoteResource(), we then set up what we want the URLs that start with api/ to redirect to the
# resource.

