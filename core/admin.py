from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Job, Bid, Contract, Reviews, Payment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Bid)
admin.site.register(Contract)
admin.site.register(Reviews)
admin.site.register(Payment)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    
    # Optionally, define a custom method to display the role
    def get_role(self, obj):
        # Handle if a user doesn't have a profile yet
        return obj.profile.role if hasattr(obj, 'profile') else 'Admin'
    get_role.short_description = 'Role'
    
    # Customize list_display to include the role
    list_display = BaseUserAdmin.list_display + ('get_role',)

# Unregister the old User admin and register your customized one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
