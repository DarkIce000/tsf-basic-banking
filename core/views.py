from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.http import JsonResponse
import json

from .models import Customer, Account, Transaction

def homepage_view(request): 
    if request.method == "POST":
        name, email = request.POST['name'], request.POST['email']
        if name and email:
            customer = Customer()
            customer.register(name=name, email=email)
            return HttpResponseRedirect(reverse('homepage'))

        return HttpResponseRedirect(reverse('homepage'))

    customers = Customer.objects.all()
    return render(request, "core/homepage.html", {
        "customers": customers,
        })


def customer_view(request, id):
    try:
        customer1 = Customer.objects.get(id=id)
    except Customer.DoesNotExist: 
        error = "Error: No such customer"
        return render(request, "core/customer.html", {
            "error": error,
            "customer1":None,
            "customer2":None
        })

    if request.method == "json" :
        return JsonResponse({
            customer1.id
        })

    try:
        customer2 = Customer.objects.all().exclude(id=id)
    except Customer.DoesNotExist:
        error = "Error: No any other customers"
        return render(request, "core/customer.html", {
            "error": error,
            "customer1":customer1,
            "customer2":None
        })

    return render(request, "core/customer.html", {
        "error" : None,
        "customer1": customer1,
        "customer2": customer2,
    })


def transaction_view(request, customer1):
    request_dict    = json.load(request)
    customer        = Customer(id=customer1)
    if request.method == "POST":
        amount          = int(request_dict['amount'])
        recievers_ids   = request_dict['recievers_ids']
        for id in recievers_ids:
            transaction = Transaction()
            try:
                transaction.transfer_money(
                    customer1_id=customer.id,
                    customer2_id=int(id),
                    amount=amount
                    )
            except Transaction.DoesNotExist as o :
                return JsonResponse({
                    "message": "some Error occured"
                })
            print(id)
        return JsonResponse({ "success": "success is waiting"})