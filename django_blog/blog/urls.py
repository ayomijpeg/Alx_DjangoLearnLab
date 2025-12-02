from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    CommentUpdateView, 
    CommentDeleteView,
    CommentCreateView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Custom Views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Built-in Auth Views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Advanced Features URLs
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='post-by-tag'),
    path('search/', PostListView.as_view(), name='search-posts'), # <--- THIS WAS MISSING

    # Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('posts/', PostListView.as_view(), name='post-list-check'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
