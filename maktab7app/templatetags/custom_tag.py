# blog/templatetags/custom_tags.py
from django import template
from ..models import Post  # Adjust the import based on your model's location

register = template.Library()

@register.inclusion_tag('maktab7app/recent_post.html')
def show_latest_posts(count=6):
    latest_posts = Post.objects.filter(status=1).order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}
