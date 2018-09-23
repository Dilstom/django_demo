from django.contrib import admin

from .models import User
# from .models import User, UserPremium

class userAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# # Register your models here.
admin.site.register(User, userAdmin)
# admin.site.register(UserPremium)
