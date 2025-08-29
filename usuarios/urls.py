from django.urls import path
from .views import LoginView, CadastroView, ListUsuario


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('usuarios/', ListUsuario.as_view(), name='list-usuarios')
]

