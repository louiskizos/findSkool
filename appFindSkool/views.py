
from .models import Skool,User,Degree
from .serializer import SkoolSerializer, UserSerializer, DegreeSerializer
from django.contrib.auth import logout
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


from rest_framework import generics,mixins, authentication, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView

# Create your views here.


class SchoolListAPIView(generics.ListAPIView):
     
     queryset = Skool.objects.all()#.order_by()[:1]
     serializer_class = SkoolSerializer


class LoginView(generics.GenericAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Msg": "Connected !", "token": token.key})
        else:
            return Response({"error": "Identifiant invalid"})


class LogoutView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Effectue la déconnexion de l'utilisateur
        logout(request)
        return Response({"Msg": "logout successfuly !"}, status=200)


class UserListAPIView(generics.ListAPIView):
     
     queryset = User.objects.all() 
     serializer_class = UserSerializer


class SkoolMixin(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin
):
    queryset = Skool.objects.all()
    serializer_class = SkoolSerializer
    lookup_field = 'pk'
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('designationEcole')
        email = request.data.get('email')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists."})
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email with this name already exists."})
        # Create user
        user = User.objects.create_user(
            username=username,
            password="123456",
            email=email
        )
        user.is_staff = True
        user.save()

        skool = Skool.objects.create(
            user=user,
            image=request.data.get('image'),
            designationEcole=username,
            arreteMin=request.data.get('arreteMin'),
            adresse=request.data.get('adresse'),
            telephone=request.data.get('telephone'),
            email=email,
            typesEcole=request.data.get('typesEcole'),
            promoteur=request.data.get('promoteur'),
            biographie=request.data.get('biographie')
        )
        serializer = self.get_serializer(skool)
        return Response(serializer.data) 
    
    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):

        return self.destroy(request, *args, **kwargs)

class DegreeCreateAPIView(generics.GenericAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [permissions.IsAuthenticated]  # S'assure que l'utilisateur est connecté

    def post(self, request, *args, **kwargs):

        pk_user = request.user.pk
        designation = request.data.get('designation')
        # Vérifie si l'école existe
        try:
            skool_pk = Skool.objects.get(pk=pk_user)
        except Skool.DoesNotExist:
            return Response({"error": "École non trouvée"}, status=404)

        # Crée le degree
        degree = Degree.objects.create(
            skool=skool_pk,
            designation=designation
        )
        serializer = self.get_serializer(degree)
        return Response(serializer.data, status=201)
