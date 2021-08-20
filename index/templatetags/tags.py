from django.template import Library
from index.forms import SubscriberForm
register = Library()


@register.simple_tag
def get_subscriber():
    return SubscriberForm