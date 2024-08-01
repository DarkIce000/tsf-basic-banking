from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"), 
    path("u/<int:id>/", views.customer_view, name="customer"),
    path("u/<int:customer1>/transaction/", views.transaction_view, name="transaction")
]