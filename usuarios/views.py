from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from usuarios.models import Usuario
from django.contrib.auth.hashers import make_password
from .serializers import UsuarioSerializer
from .permissions import IsAdmin, IsAdminOrVendedor, IsVendedor
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        senha = request.data.get ('password')
        
        
        if not email or not senha:
            return Response({'erro': 'Email e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)
        
        usuario = authenticate(request, email=email, password=senha)
        
        if usuario is None:
            return Response({'erro': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh =  RefreshToken.for_user(usuario)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'usuario': {
                'id': usuario.id,
                'email': usuario.email,
                'nome': usuario.nome,
                'tipo': usuario.tipo
            }
        }, status=status.HTTP_200_OK )
        
        

class CadastroView(APIView):
    def post(self, request):
        email = request.data.get('email')
        senha = request.data.get ('password')
        nome = request.data.get('nome')
        
        if not email or not senha or not nome:
            return Response({'erro': 'Todos os campos são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Usuario.objects.filter(email=email).exists():
            return Response({'erro': 'Email já cadastrado!'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        usuario = Usuario.objects.create(
            email = email,
            nome = nome,
            password = make_password(senha)
        )
        
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'mensagem': 'Usuário criado com sucesso!',
            'usuario': {
                'id': usuario.id,
                'email': usuario.email,
                'nome' : usuario.nome
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        }, status=status.HTTP_201_CREATED)


class ListUsuario(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdmin]
