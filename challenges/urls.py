from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.redirect_monthly_challenges),
    path("<str:month>", views.monthly_challenges, name="month-challenge"),
    path("", views.show_month_list, name="index")
]
