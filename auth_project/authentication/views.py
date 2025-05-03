# 6. authentication/views.py (COMPLETE FILE)
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from .tokens import email_verification_token

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate verification token
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = email_verification_token.make_token(user)
        
        # Create verification link
        verification_link = f"http://{settings.SITE_DOMAIN}/api/auth/verify-email/{uid}/{token}/"
        
        # Send email
        email_subject = 'Activate Your Account'
        email_body = f"""
        Hi {user.username},
        
        Please click the link below to verify your email:
        
        {verification_link}
        
        If you didn't register with us, please ignore this email.
        
        Thank you!
        """
        
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully. Please check your email to verify your account."
        }, status=status.HTTP_201_CREATED)


class VerifyEmailView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            
            if email_verification_token.check_token(user, token):
                user.email_verified = True
                user.save()
                
                # Create auth token
                token, created = Token.objects.get_or_create(user=user)
                
                return Response({
                    "message": "Email verified successfully.",
                    "token": token.key,
                    "user": UserSerializer(user).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Verification link is invalid or expired."}, 
                                status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({"error": f"Verification failed: {str(e)}"}, 
                            status=status.HTTP_400_BAD_REQUEST)


class ResendVerificationEmailView(APIView):
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            user = User.objects.get(email=email)
            
            if user.email_verified:
                return Response({"message": "Email is already verified."}, status=status.HTTP_200_OK)
                
            # Generate verification token
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = email_verification_token.make_token(user)
            
            # Create verification link
            verification_link = f"http://{settings.SITE_DOMAIN}/api/auth/verify-email/{uid}/{token}/"
            
            # Send email
            email_subject = 'Activate Your Account'
            email_body = f"""
            Hi {user.username},
            
            Please click the link below to verify your email:
            
            {verification_link}
            
            If you didn't register with us, please ignore this email.
            
            Thank you!
            """
            
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            
            return Response({"message": "Verification email has been resent."}, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            # For security reasons, don't reveal that the email doesn't exist
            return Response({"message": "If your email exists in our system, we've sent a verification link."}, 
                            status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                if not user.email_verified:
                    return Response({'error': 'Please verify your email before logging in.'}, 
                                   status=status.HTTP_401_UNAUTHORIZED)
                                   
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserSerializer(user).data
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass
        
        logout(request)
        return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
