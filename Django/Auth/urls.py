from django.urls import path
from Auth import views

urlpatterns =[
    # path('Auths/', views.auths_list)
    # path('Auths/<id>', views.auth_details)
    # path('Auths/email/<email>')
]

'''
GET     Auths/: get all Auths
GET     Auths/id: get an auth by id
GET     Auths/email/[email]: find all Auths by email
POST    Auths/: save an auth
PUT     Auths/[id]: update a auth by id
DELETE  Auths/[id]: delete a auth by id
---------------------------------To remove - its dangerouse------------------------------DELETE  Auths/: delete all Auths
'''
