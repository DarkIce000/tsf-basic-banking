from django.contrib import admin
from core.models import Customer, Account, Transaction

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transaction)