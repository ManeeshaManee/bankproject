from django.contrib import admin
from .models import Departments,Account_type, Booking, Country, City

# Register your models here.
admin.site.register(Departments)
admin.site.register(Account_type)
# admin.site.register(District)
# admin.site.register(Branchname)
admin.site.register(Country)
admin.site.register(City)





class BookingAdm(admin.ModelAdmin):
    list_display = ('id', 'u_name','date_birth', 'u_phone', 'u_email','u_address','city','country','ac_type','booking_date','booked_on','DEBIT_CARD','CREDIT_CARD','CHEQUE_BOOK')


admin.site.register(Booking, BookingAdm)
