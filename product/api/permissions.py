from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'شما باید نویسنده ی این کامنت باشید'
    my_safe_methods = ['GET',
                       'PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        return obj.user == request.user
