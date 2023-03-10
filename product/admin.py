from django.contrib import admin
from .models import product, Logo
# Register your models here.
admin.site.register(Logo)
admin.site.site_header = "TrustBuy administration website"
admin.site.site_title = "site administration"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'seller_name')
    search_fields = ('name', 'description', 'seller_name__username')

admin.site.register(product, ProductAdmin)







