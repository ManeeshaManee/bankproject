from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments
from .forms import BookingForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def branches(request):
    return render(request, "branches.html")


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, "booking.html", dict_form)



def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, "departments.html", dict_dept)



