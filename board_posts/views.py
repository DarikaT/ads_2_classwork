from django.views.generic import ListView 
from .models import Post

class IndexPageView(ListView):
    model = Post
    template_name = 'index.html'