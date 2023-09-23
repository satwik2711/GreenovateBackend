from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Factor)
admin.site.register(SubFactor)
admin.site.register(SubSubFactor)
admin.site.register(Organisation)
admin.site.register(EmissionRecord)

