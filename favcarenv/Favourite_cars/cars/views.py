from django.shortcuts import  get_object_or_404,render
from.models import Cars, Contact
from .forms import ContactForm

# Create your views here.
def cars_list(request):
    cars = Cars.objects.all()
    return render(request,'Car_list.html',{'cars':cars})
def cars_detail(request,pk):
    car = get_object_or_404(Cars,pk=pk)
    return render(request, 'Car_detail.html',{'car':car})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', { 'form':form})