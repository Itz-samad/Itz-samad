from django.contrib import admin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Usera

class UseraAdmin(BaseUserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_no', 'birthdate', 'gender')}),
      (_('Documents'), {'fields': ('doc_type', 'cac', 'nepc', 'nepc_id')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )

#   add_fieldsets = (
#       (None, {
#           'classes': ('wide', ),
#           'fields': ('email', 'password1', 'password2'),
#       }),
#   )


  list_display = ['first_name', 'last_name', 'email', 'role']
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email')

admin.site.register(Usera, UseraAdmin)

