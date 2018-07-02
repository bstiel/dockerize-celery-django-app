import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings


logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def index(request, format=None):
    return Response([])


@api_view(['GET'])
def get(request, format=None):
    return Response({})
