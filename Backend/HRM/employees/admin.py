from django.contrib import admin
from .models import Employee
from guardian.admin import GuardedModelAdmin


class EmployeeAdmin(GuardedModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)









# admin.site.unregister(User)
# admin.site.unregister(Group)
#h
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         if not is_superuser:
#             form.base_fields['username'].disabled = True
#             form.base_fields['is_superuser'].disabled = True
#             form.base_fields['user_permissions'].disabled = True
#             form.base_fields['groups'].disabled = True
#         return form
#
# class ReadWriteOnlyModelAdmin:
#     def has_add_permission(self, request, obj = None):
#         if request.user.has_perm('employees.can_add_employee'):
#             return True
#         return False
#     def has_change_permission(self, request, obj=None):
#         if request.user.has_perm('employees.can_change_employee'):
#             return True
#         else:
#             return False
#     def has_delete_permission(self, request, obj=None):
#         if request.user.is_superuser:
#             return True
#         return False
#     def has_view_permission(self, request, obj=None):
#         return True
#
# @admin.register(Employee)
# class EmployeeAdmin(ReadWriteOnlyModelAdmin, admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         if not is_superuser:
#             form.base_fields['user'].disabled = True
#
#             form.base_fields['salary'].empty_label = True
#             # exclude = ['salary', 'date_left', 'date_hired']
#         return form


