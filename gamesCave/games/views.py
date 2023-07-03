from django.shortcuts import render

# Create your views here.

def home(request):
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
    
    return render(request, 'home.html', {'movies': movies})