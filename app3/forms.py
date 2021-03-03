from django import forms
from app3.models import Ingrediant

class IngrediantForm(forms.ModelForm):

    class Meta:
        model = Ingrediant
        fields = ['ing_name',
                    'ing_description',
                    'ing_price',
                    'ing_photo',
                    'ing_weight',
                    'ing_foodgroup',
                    'ing_dietarygroup',
                    'published_date']
