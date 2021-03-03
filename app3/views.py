from django.shortcuts import render, redirect
from app3.models import Ingrediant
from django.http import HttpResponse
from app3.forms import IngrediantForm
from app3.models import Ingrediant

# Create your views here.
def index(request):
    ing_list = Ingrediant.objects.order_by('ing_name')
    ing_dict = {'raw_ing':ing_list}
    return render(request,'app3/index.html', context=ing_dict)

#def other(request):
    #return render(request,'app3/other.html')

def relative(request):
    return render(request,'app3/relative_url_templates.html')



def Ingrediant_image_view(request):

    if request.method == 'POST':
        form = IngrediantForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/app3/success')
    else:
        form = IngrediantForm()
    return render(request, 'app3/ingrediant_image_form.html', {'form' : form})


def success(request):
    return HttpResponse('successfully uploaded')
    
#this view is where we return thr ingrediant to the page.
def display_ingrediant_images(request):

    if request.method == 'GET':

        # getting all the objects of Ingrediant.
        ing = Ingrediant.objects.all()
        return render(request, 'app3/display_inge_images.html',
                     {'actual_images' : ing})
