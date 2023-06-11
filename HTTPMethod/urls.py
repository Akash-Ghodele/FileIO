from django.urls import path
from .views import *

urlpatterns = [
    path('emp/', EmployeeView.as_view(), name='emp'),
    path('emp/<int:id>/', EmployeeInfo.as_view())
]
