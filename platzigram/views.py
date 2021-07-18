""" Platzigram views """

# Python
import pdb

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """ Returns a greeting """
    return HttpResponse(f"Hey! it's {datetime.now().strftime('%b %dth, %Y - %H:%M hrs')}")

def order_numbers(request):
    """ Gets numbers array from url and return them ordered """
    pdb.set_trace()
    return HttpResponse(request)