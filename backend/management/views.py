from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from management.mixins import MixinViewSet
from management.utils.csrf import CsrfExemptSessionAuthentication
from django.db.migrations.recorder import MigrationRecorder


class InstallView(MixinViewSet):
    http_method_names = ['get']
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @swagger_auto_schema(
        operation_description='Initial Project',
        tags=['initial'],
        responses={
            status.HTTP_302_FOUND: openapi.Response(''),
        },
    )
    def get(self, request, format=None):
        MigrationRecorder.Migration.objects.all().count()
        return HttpResponseRedirect('/')
