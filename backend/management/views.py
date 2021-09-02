from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import uuid
from management.mixins import MixinViewSet
from management.utils.csrf import CsrfExemptSessionAuthentication


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
        reply = {
            'success': False,
            'message': "unknown error"
        }
        return Response(reply, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
