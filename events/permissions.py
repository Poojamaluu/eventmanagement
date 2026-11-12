from rest_framework.permissions import BasePermission

class IsOrganizerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True

        else:
            return request.user.is_authenticated and request.user.role=="organizer"


    def has_object_permission(self,request,view,obj):
        if request.method=="GET":
            return True
        else:
            return obj.organizer==request.user


