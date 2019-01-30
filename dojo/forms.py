from django import forms

from dojo.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }


# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_length_3_validator])
#     content = forms.CharField(widget=forms.Textarea)
#
#     def save(self, commit=True):
#         post = Post(**self.cleaned_data)
#         if commit:
#             post.save()
#         return post