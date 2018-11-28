from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypieapp.models import Entry
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields, utils



class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        fields = ['username']
        filtering = {
            'username': ALL,
        }
        include_resource_uri = False

class EntryResource(ModelResource):
    # Maps `Entry.user` to a Tastypie `ForeignKey` field named `user`,
    # which gets serialized using `UserResource`. The first appearance of
    # 'user' on the next line of code is the Tastypie field name, the 2nd
    # appearance tells the `ForeignKey` it maps to the `user` attribute of
    # `Entry`. Field names and model attributes don't have to be the same.
   # user = fields.ForeignKey(UserResource, 'user')
    user = fields.ToOneField(UserResource, attribute='user', null=True, full=True)

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }