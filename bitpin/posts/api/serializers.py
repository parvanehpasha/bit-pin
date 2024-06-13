from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from bitpin.posts.models import Post, RatePost


class CreatePostSerializer(serializers.Serializer):
    """
    validate input and create new post
    """
    title = serializers.CharField()
    body = serializers.CharField()

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.get('user')
        title = validated_data.get('title')
        body = validated_data.get('body')
        Post.objects.create(user=user, title=title, body=body)
        return validated_data


class ListPostSerializer(ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Post
        fields = ['title', 'body', 'user', 'rate_ave']


class RatePostSerializer(serializers.Serializer):
    """
    validate input for add rate to post
    """
    post = serializers.CharField()
    rate = serializers.IntegerField()

    def validate(self, attrs):
        user = self.context['request'].user
        post = attrs.get('post')
        attrs['user'] = user
        post = Post.objects.filter(id=post)
        if not post.exists():
            raise serializers.ValidationError('this post not found')
        attrs['post'] = post.first()
        return attrs

    def create(self, validated_data):
        user = validated_data.get('user')
        post = validated_data.get('post')
        rate = validated_data.get('rate')
        RatePost.objects.create(user=user, post=post, rate=rate)
        return validated_data


