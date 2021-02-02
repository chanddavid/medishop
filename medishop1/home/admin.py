from django.contrib import admin

from .models import Company, Medicine, MedicalDetails, Employee, Customer, EmployeeSalary, Bill, BillDetails, \
    CustomerRequest, CompanyBank, CompanyAccount, EmployeeBank

# Register your models here.

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(EmployeeBank)
