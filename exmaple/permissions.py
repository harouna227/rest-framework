from rest_framework import permissions


class IsOwerOrReadOnly(permissions.BasePermission):
    """
    Autorisation personnalisée pour autoriser uniquement 
    les propriétaires d'un objet à le modifier(delete or update).
    """

    def has_object_permission(self, request, view, obj):
        # Les autorisations de lecture sont autorisées pour toute demande,
        # donc nous autoriserons toujours les requêtes GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Les autorisations d'écriture ne sont accordées qu'au propriétaire de l'extrait.
        return obj.owner == request.user