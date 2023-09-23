from . import views
from django.urls import path

urlpatterns = [
    path('emission_delta_tips/<int:org_id>/<int:year1>/<int:year2>/', views.get_emission_delta_tips),
    path('create_tip/', views.create_tip),
]