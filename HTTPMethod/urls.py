from django.urls import path
from .views import *

urlpatterns = [
    #path('emp/', EmployeeView.as_view(), name='emp'),
    #path('emp/<str:id>/', EmployeeInfo.as_view()),
    path('file/<str:path>/', FileOperation.as_view()),
]
