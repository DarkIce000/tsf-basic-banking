from core.models import *

c1 = Customer(name="aarav", email="aarav2@gmail.com")
c1.save()
c2 = Customer(name="arghya", email="arghya@gmail.com")
c2.save()

t1 = Transaction()
t1.transfer_money(c1.id, c2.id, 5000)
t1.save()
