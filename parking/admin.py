from django.contrib import admin
from parking.models import Registration,Contact,Complaint
from parking.models import VehicleEntry
from parking.models import VehicleExit

admin.site.register(Registration)
admin.site.register(Contact)
admin.site.register(Complaint)
admin.site.register(VehicleEntry)
admin.site.register(VehicleExit)