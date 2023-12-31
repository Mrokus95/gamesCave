from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
    else:
        user_first_name = ""
    movies = [
        {
            'name': 'Mass Effect',
            'des': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit porro et veniam excepturi, eaque voluptatem impedit nulla laboriosam facilis ut laboriosam libero!',
            'image': 'static/games/images/mass-effect.jpg'
        },
        {
            'name': 'Mass Effect 2',
            'des': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit porro et veniam excepturi, eaque voluptatem impedit nulla laboriosam facilis ut laboriosam libero!',
            'image': 'static/games/images/mass-effect.jpg'
        },
        {
            'name': 'Mass Effect 3',
            'des': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit porro et veniam excepturi, eaque voluptatem impedit nulla laboriosam facilis ut laboriosam libero!',
            'image': 'static/games/images/mass-effect.jpg'
        },
        {
            'name': 'Mass Effect 4',
            'des': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit porro et veniam excepturi, eaque voluptatem impedit nulla laboriosam facilis ut laboriosam libero!',
            'image': 'static/games/images/mass-effect.jpg'
        },
        {
            'name': 'Mass Effect 5',
            'des': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit porro et veniam excepturi, eaque voluptatem impedit nulla laboriosam facilis ut laboriosam libero!',
            'image': 'static/games/images/mass-effect.jpg'
        }
    ]
    
    return render(request, 'home.html', {'movies': movies, 'user_first_name': user_first_name})