from django.contrib import admin

from bitpin.posts.models import Post, RatePost


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'body', 'created_at']


class RatePostAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'rate']


admin.site.register(Post, PostAdmin)
admin.site.register(RatePost, RatePostAdmin)

