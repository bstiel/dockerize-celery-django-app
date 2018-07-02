import logging
import os
import json

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from worker.tasks import fetch_data_from_quandl


logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def index(request, format=None):
    if request.method == 'POST':
        fetch_data_from_quandl.s(
            database_code=request.data['database_code'],
            dataset_code=request.data['dataset_code']).delay()
        return Response('', status=status.HTTP_201_CREATED)
    files = [] if not os.path.exists(settings.DATA_PATH) else os.listdir(settings.DATA_PATH)
    return Response(files)


@api_view(['GET'])
def get(request, slug, format=None):
    path = os.path.join(settings.DATA_PATH, slug)
    if not os.path.exists(path):
        logger.info(f'{path}: not found')
        return Response('', status=status.HTTP_404_NOT_FOUND)
    logger.info(f'{path}: read content')
    with open(path, 'r') as f:
        s = f.read()
    try:
        s = json.loads(s)
        logger.info(f'{path}: content is json')
    except:
        logger.info(f'{path}: content is not json')
    return Response(s)
