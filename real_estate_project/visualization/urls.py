# visualization/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.visualization_view, name="visualization"),
    path("visualization/", views.visualization_view, name="visualization"),
    # path("choropleth/", views.choropleth_view, name="choropleth"),
    path("price_query/", views.price_query_view, name="price_query"),
]
