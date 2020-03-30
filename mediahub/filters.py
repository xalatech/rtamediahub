import django_filters

from mediahub.models import Post, Category
from datetime import datetime, timedelta


class PostFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(label='Category',
                                                queryset=Category.objects.all(),
                                                empty_label="All Posts", null_value=0)
