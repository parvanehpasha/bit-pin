from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from bitpin.users.models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    mobile = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """ Validate the username and password. """
        username = attrs.get('username')
        password = attrs.get('password')
        mobile = attrs.get('mobile')
        confirm_password = attrs.get('confirm_password')
        if User.objects.filter(Q(username=username) | Q(mobile=mobile)).exists():
            raise serializers.ValidationError('username or phone number duplicate')
        elif username == password:
            raise serializers.ValidationError('The password cannot be the same as the username')
        elif password == mobile:
            raise serializers.ValidationError('The password cannot be the same as the phone number')
        elif confirm_password != password:
            raise serializers.ValidationError('The password not match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User

    def validate(self, attrs):
        """ this function validate input """
        username = attrs.get('username')
        password = attrs.get('password')

        """ authenticate the username and password"""
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.get('user')
        refresh = RefreshToken.for_user(user)
        validated_data['access_token'] = str(refresh.access_token)
        validated_data['refresh_token'] = str(refresh)
        print(validated_data)
        return validated_data
