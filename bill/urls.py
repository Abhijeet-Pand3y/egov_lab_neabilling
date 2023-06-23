from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_user, name="search_user"),
    path('display/<int:id>', views.display_users_bill, name="display_user"),
]
