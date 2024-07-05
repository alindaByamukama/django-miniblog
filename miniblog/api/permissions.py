from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # a custom permission to allow authors of an obj to edit

    def has_object_permission(self, request, view, obj):
        # allow get, head, options reqs
        if request.method in permissions.SAFE_METHODS:
            return True

        # author only
        return obj.author == request.user
