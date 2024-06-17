from django.forms import ModelForm
from .models import Poem

class PoemForm(ModelForm):
    class Meta:
        model = Poem
        fields = "__all__"