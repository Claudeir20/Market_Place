from rest_framework.permissions import BasePermission



from rest_framework.permissions import BasePermission

class IsVendedor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'vendedor'


class IsCliente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'cliente'


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.tipo == 'admin' and
            request.user.is_staff
        )



class IsAdminOrVendedor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                (request.user.tipo == 'admin' and request.user.is_staff) or
                request.user.tipo == 'vendedor'
            )
        )