from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from flask import redirect

from .models import Departments, City, Booking
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



# def person_create_view(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking')
#     return render(request, 'booking.html', {'form': form})



def person_update_view(request, pk):
    person = get_object_or_404(Booking, pk=pk)
    form = BookingForm(instance=booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'booking.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'dropdown.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
