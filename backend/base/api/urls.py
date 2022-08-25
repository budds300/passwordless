from django.urls import path
from . import views
from .views import register_page, home_page, login_page, generate_otp, check_otp

# from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import ( TokenObtainPairView,  TokenRefreshView,)


urlpatterns = [
    path('',views.getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_page, name="register"),
    path('check/', check_otp, name="check_otp"),
    path('login/', login_page,  name="login"),
    path('otp/<int:pk>/<uuid>/', generate_otp),
    path('home/', home_page)

]