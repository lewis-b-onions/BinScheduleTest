from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

# Creating resource

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()

# The queryset is what models the resource in concerned with. In this case, this is the created Note model in the
#  models.py file returning all note objects.

# naming the resource_name to note will be used in the URLs

# This file contains the idea of resources used as a middle class that sites between our URLs and our models.
# When a user makes a request to an endpoint. Depending on the URL, the user will be redirected to a particular resource,
# which will then perform the appropriate CRUD action on the model