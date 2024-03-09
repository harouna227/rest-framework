from django.urls import path, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

""" Methode de configuration d'URL manuel """
# Ici je créer plusieurs views à partir de classe ViewSet
# En liant les methodes HTTP à l'action requise pour chaque view
# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),

#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),

#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
# ])

""" Methode de configuration d'URL avec la classe Router"""
# Créer un routeur et enregister nos viewSet avec
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# URLs VBSC
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),

#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),

#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ])

# urlpatterns = format_suffix_patterns(urlpatterns)