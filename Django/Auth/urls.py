from django.urls import path
from Auth import views

urlpatterns =[
    path('Auths/', views.auth_list),
    path('Auths/<id>', views.auth_details),
    path('Auths/<user_name>', views.auth_by_username),
]
