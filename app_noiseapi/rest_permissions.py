from rest_framework import permissions

class DisableOptionsPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method == 'OPTIONS':
			return False
		return True
