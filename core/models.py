from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.utils import IntegrityError

class Customer(models.Model):
    name  = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)

    def save(self, *args, **kwargs):
        customer_id = not self.pk
        super().save(*args, **kwargs)
        if customer_id: # if not existing customer then create an account for him/her
            account = Account(customer=self)
            account.save()
    
    def register(self, name, email):
        self.name = name
        self.email = email
        self.save()

    def __str__(self):
        return f'name:{self.name}, email:{self.email}'


class Account(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    balance  = models.IntegerField(default=10000)
    
    def __str__(self):
        return f'customer name: {self.customer.name}, balance:{self.balance}'


class Transaction(models.Model):
    amount    = models.IntegerField(default=0, blank=False)
    customer1 = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sender")
    customer2 = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reciever")
    timestamp = models.DateTimeField(auto_now_add=True)

    def transfer_money(self, customer1_id, customer2_id, amount=0):
        try:
            c1  = Customer.objects.get(id=customer1_id)
            c2  = Customer.objects.get(id=customer2_id)
        except IntegrityError:
            raise Exception("Data Error")
        except Customer.DoesNotExist:
            raise Exception('Customer Does not exist')

        if int(c1.account.balance) >= amount: # checking for sufficient amount in the account
            self.amount    = amount
            self.customer1 = c1
            self.customer2 = c2
            self.save()
            # update the balance of the customer1 
            c1.account.balance = int(c1.account.balance)-amount
            c2.account.balance = int(c2.account.balance)+amount
            c1.account.save()
            c2.account.save()
        else:
            raise ValueError("Insufficient Money")
        

    def __str__(self):
        return f'{self.customer1.name} has transfered {self.amount} to {self.customer2.name}'
