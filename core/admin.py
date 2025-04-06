from django.contrib import admin
from .models import Users, Profile, Job, Bid, Contract, Reviews, Payment
# Register your models here.
admin.site.register(Users)
admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Bid)
admin.site.register(Contract)
admin.site.register(Reviews)
admin.site.register(Payment)
