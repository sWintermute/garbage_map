from django.urls import path
from django.urls.resolvers import URLPattern

from .views import unit, clear_map
urlpatterns = [
    path('<int:n_mt>', unit),
    path('', clear_map),
]
