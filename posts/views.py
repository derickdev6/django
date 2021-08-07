# Posts views

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Everest',
        'user': 'Derick',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'pic': 'https://images.unsplash.com/photo-1556135063-eba17c48d523?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDJ8dG93SlpGc2twR2d8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
    },
    {
        'name': 'Alhil',
        'user': 'Edna',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'pic': 'https://images.unsplash.com/photo-1628038340278-9818521002ac?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDd8dG93SlpGc2twR2d8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
    },
    {
        'name': 'Bakka',
        'user': 'Dario',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'pic': 'https://images.unsplash.com/photo-1628038341191-8e7448fc8209?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDh8dG93SlpGc2twR2d8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
    },
    {
        'name': 'Yamal',
        'user': 'Joseph',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'pic': 'https://images.unsplash.com/photo-1627660692856-bc032e058cc2?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDIwfHRvd0paRnNrcEdnfHxlbnwwfHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
    }
]


def list_posts(request):
    # Lists existing posts
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <img src="{pic}" height="200">
        """.format(**post))
    return HttpResponse(content)
