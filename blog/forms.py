from django import forms

from first_django.widgets.naver_map_point_widget import NaverMapPointWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat':NaverMapPointWidget(attrs={'width':600, 'height': 300}),
        }