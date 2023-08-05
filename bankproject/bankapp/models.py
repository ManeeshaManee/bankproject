from django.db import models


# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class District(models.Model):
    dic_name = models.CharField(max_length=255)

    def __str__(self):
        return self.dic_name


class Branchname(models.Model):
    branch_name = models.CharField(max_length=255)
    dic_name = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch_name


class Account_type(models.Model):
    ac_type = models.CharField(max_length=255)

    def __str__(self):
        return self.ac_type


class Booking(models.Model):
    u_name = models.CharField(max_length=255)
    date_birth = models.DateField()
    age=models.IntegerField()
    Gender=models.CharField(max_length=255)
    u_phone = models.CharField(max_length=10)
    u_email = models.EmailField()
    u_address = models.TextField(max_length=1000)
    dic_name = models.ForeignKey(District, on_delete=models.CASCADE)
    branch_name = models.ForeignKey(Branchname, on_delete=models.CASCADE)
    ac_type = models.ForeignKey(Account_type, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    DEBIT_CARD = models.BooleanField()
    CREDIT_CARD=models.BooleanField()
    CHEQUE_BOOK=models.BooleanField()