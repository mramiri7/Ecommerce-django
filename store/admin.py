from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Profile)
admin.site.register(models.ProductComment)
