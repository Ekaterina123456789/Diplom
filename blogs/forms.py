from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Blog


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

