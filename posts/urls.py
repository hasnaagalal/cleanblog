from django.urls import path 
from .views import PostListView, PostDetailView ,PostCreateView ,PostUpdateView ,PostDeleteView
from . import views

app_name = 'posts'



urlpatterns=[   
    path('about/', views.about,name='about'),  
    path('contact/', views.contact,name='contact'), 
    path('posts/', views.posts ,name='posts'),        
    path('', PostListView.as_view(),name='home'),
    path('post-new/', PostCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete")
]


   
