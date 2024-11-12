from django.urls import path
from .views import SchoolListAPIView, UserListAPIView, LoginView, SkoolMixin,DegreeCreateAPIView,LogoutView





urlpatterns = [
    #Pour Trois
    path('', SchoolListAPIView.as_view()),
    #Pour Six
    #path('Masomo_Alea_6', SchoolListAPIView.as_view()),
    # List all users
    path('List-User/', UserListAPIView.as_view()),
    # path('List-User/<int:pk>/', UserMixin.as_view()),
    # #LogIn 
    path('Login/', LoginView.as_view()),
    # # Token
    # path('Token/', CustomTokenObtainPairView.as_view()),
    # #LogOut
    path('LogOut/', LogoutView.as_view()),
    # Insert school and user ===> default username = nameschool and pwd = 1234 
    path('Insert-Skool/', SkoolMixin.as_view()),
    # Insert school and user ===> default username = nameschool and pwd = 1234 
    path('Insert-Degree/', DegreeCreateAPIView.as_view()),
    # # Update school
    # path('Update-Masomo/<int:pk>/', MasomoMixin.as_view()),
    # # Delete school
    # path('Delete-Masomo/<int:pk>/', MasomoMixin.as_view()),
    # # Classe Masomo
    # path('Insert-Classe-Masomo/', MasomoClasseMixin.as_view()),
    # path('Update-Classe-Masomo/<int:pk>/', MasomoClasseMixin.as_view()),
    # path('Delete-Classe-Masomo/<int:pk>/', MasomoClasseMixin.as_view()),
] 