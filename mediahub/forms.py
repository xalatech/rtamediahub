from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from mediahub.models import Post


class PostForm(forms.ModelForm):
    success_url = reverse_lazy('index')

    class Meta:
        model = Post
        fields = ('headline', 'description', 'tags',
                  'category', 'upload', 'thumb', 'slug')
        widgets = {'thumb': forms.HiddenInput(), 'slug': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(PostForm, self).post(request, *args, **kwargs)



class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
