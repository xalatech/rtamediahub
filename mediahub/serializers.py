from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['headline', 'description', 'tags',
                  'category', 'posttype', 'upload', 'thumb', 'slug']