from django.forms import ModelForm
from serie.models import Serie

# Create the form class.
class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = ['nome', 'sinopse', 'num_episodios', 'data_lancamento']