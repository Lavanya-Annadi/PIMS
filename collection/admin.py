from django.contrib import admin

# Register your models here.
from collection.models import collection, row

admin.site.register(row)
admin.site.register(collection)
#admin.site.register(collection_group)

