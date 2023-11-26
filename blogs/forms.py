from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Blog, Advertisement, Review
from django import forms
from captcha.fields import CaptchaField


class ReviewForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Review
        fields = ['body',]

        labels = {
            'body': 'Оставьте комментарий',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'image', 'video', 'source_link', 'tags']
        widgets = {
            'tags': CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class AdvertisementForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Advertisement
        fields = ['text', 'image', 'contacts']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
