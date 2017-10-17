from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import \
    (AllowAny,
     IsAdminUser,
     IsAuthenticated,
     IsAuthenticatedOrReadOnly)

class IsOwnerOfBasket(BasePermission):
    message = '.فقط صاحب این اکانت توانایی ویرایش سبد خرید را دارد'
    my_safe_methods = ['GET',
                       'PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif obj.current_user == request.user:
            return True
        else:
            return False


class UserDetailPermissions(BasePermission):
    my_safe_methods = ['GET',
                       'PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif obj.user == request.user:
            return True
        else:
            return False

