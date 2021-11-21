from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create your views here.
class GetTokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, credenciales):
        data = super().validate(credenciales)
        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['id'] = self.user.id
        #     'first_name': self.user.first_name,
        #     'last_name': self.user.last_name,
        #     'is_superuser': self.user.is_superuser,
        #     'is_active': self.user.is_active,
        return data