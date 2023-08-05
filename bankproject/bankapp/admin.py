from django.contrib import admin
from .models import Departments,District,Branchname,Account_type,Booking

# Register your models here.
admin.site.register(Departments)
admin.site.register(Account_type)
admin.site.register(District)
admin.site.register(Branchname)


class BookingAdm(admin.ModelAdmin):
    list_display = ('id', 'u_name','date_birth', 'u_phone', 'u_email','u_address','dic_name','branch_name','ac_type','booking_date','booked_on','DEBIT_CARD','CREDIT_CARD','CHEQUE_BOOK')


admin.site.register(Booking, BookingAdm)