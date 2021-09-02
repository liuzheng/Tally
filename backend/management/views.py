from django.http import HttpResponseRedirect
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from management.mixins import MixinViewSet
from management.utils.csrf import CsrfExemptSessionAuthentication
from django.contrib.auth.models import User


class SuperuserView(MixinViewSet):
    http_method_names = ['get']
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @swagger_auto_schema(
        operation_description='Create Superuser if it is not exist',
        tags=['initial'],
        responses={
            status.HTTP_302_FOUND: openapi.Response(''),
        },
    )
    def get(self, request, format=None):
        if User.objects.filter(is_superuser=True).count() == 0:
            User.objects.create_superuser('admin', '', 'admin')
        return HttpResponseRedirect('/')
