from accounts.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','password','email','first_name','last_name','role','phone']
        read_only_fields = ['id',]

    def create(self, validated_data):#password hashing
        u= CustomUser.objects.create_user(**validated_data)
        u.save()
        return u