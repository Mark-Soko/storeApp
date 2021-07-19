from django.db.models import fields
import django_filters
from .models import *

class productFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name','category']
