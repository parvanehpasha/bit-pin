from django.urls import path
from .api import views


urlpatterns = [
    path('create-post/', views.APICreatePostView.as_view(), name='create_post'),
    path('list-post/', views.ListPostView.as_view(), name='list_post'),
    path('rate-post/', views.RatePostView.as_view(), name='rate_post'),
]
