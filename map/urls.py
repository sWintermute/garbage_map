from django.urls import path
from django.urls.resolvers import URLPattern

from .views import district_all, unit, clear_map

urlpatterns = [
    path('district/<str:district>', district_all),
    path('<int:n_mt>', unit),
    path("/map", clear_map),
]
