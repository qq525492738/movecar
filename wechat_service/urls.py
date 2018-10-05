from django.urls import path
from .views import AuthView, verify, Reply

urlpatterns = [
    path('', AuthView.as_view()),
    path('reply', Reply.as_view()),
    #path('', verify_url),
	path('MP_verify_WUPZbZ5M3JyEfpYE.txt', verify),
]
