from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Ingrediant(models.Model):
        FRUIT = 'FR'
        VEGETABLE = 'VEGT'
        CARBOHYDRATE = 'CARBS'
        PROTEIN = 'PROT'
        DAIRY = 'DARY'
        FATS = 'FT'
        OILS = 'OL'
        FOOD_GROUPS = (
        (FRUIT, 'Fruits'),
        (VEGETABLE, 'Vegetable'),
        (CARBOHYDRATE, 'Carbohydrate'),
        (PROTEIN, 'Protein'),
        (DAIRY, 'Dairy'),
        (FATS, 'Fats'),
        (OILS, 'Oils'),
    )

        VEGAN = 'VE'
        VEGETARIAN = 'VTRN'
        HALAL = 'HLL'
        KOSHER = 'KSH'
        PESCATARIAN = 'PSC'
        DIETARY_GROUPS = (
        (VEGAN, 'Vegan'),
        (VEGETARIAN, 'Vegetarian'),
        (HALAL, 'Halal'),
        (KOSHER, 'Kosher'),
        (PESCATARIAN, 'Pescatarian'),
    )
        ing_name = models.CharField(max_length=64,unique=True)
        ing_description = models.CharField(max_length=64,null=True)
        ing_price = models.DecimalField(max_digits=5, decimal_places=2)
        ing_weight = models.DecimalField(max_digits=5, decimal_places=2)
        ing_photo = models.ImageField(upload_to='images/', max_length=254, null=True)
        ing_foodgroup = models.CharField(max_length=64,choices=FOOD_GROUPS)
        ing_dietarygroup = models.CharField(max_length=64,choices=DIETARY_GROUPS)
        published_date = models.DateTimeField(blank=True, null=True)


        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.ing_photo,self.ing_photo
