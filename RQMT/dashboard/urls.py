from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_view,name="home"),

    # Machine Requirement
    path('machinerequirement/', views.machinerequirement_view, name="machinerequirement"),
    # Module Requirement
    path('modulerequirement/', views.modulerequirement_view, name="modulerequirement"),
    path('modulerequirement/create/', views.modulerequirementcreate_view, name="modulerequirementcreate"),
]