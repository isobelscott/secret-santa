from django.contrib import admin

# Register your models here.

from .models import Person, Party, Group, Wishlist, Hat

admin.site.register(Person)
admin.site.register(Party)
admin.site.register(Group)
admin.site.register(Wishlist)
admin.site.register(Hat)