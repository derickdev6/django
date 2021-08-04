""" Platzigram views """

# Python
import pdb
import json

# Django
from django.http import HttpResponse
from django.http.response import JsonResponse

# Utilities
from datetime import datetime


def hello_world(request):
    """ Returns a greeting """
    return HttpResponse(f"Hey! it's {datetime.now().strftime('%b %dth, %Y - %H:%M hrs')}")


def hi(request):
    arr = sorted([int(i) for i in request.GET['numbers'].split(',')])

    data = {
        'status': 'ok',
        'numbers': arr,
        'message': 'Ints sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')
