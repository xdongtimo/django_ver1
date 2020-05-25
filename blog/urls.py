#from django.urls import path
#from . import views

#urlpatterns = [
 #   path('', views.PostListView.as_view(), name='blog'),
   # path('<int:id>/', views.PostDetailView.as_view(), name='post'),]

from django.urls import path
from .models import Post
from . import views
from django.views.generic import ListView

urlpatterns = [
   path('', ListView.as_view(
      queryset = Post.objects.all().order_by('-data'),
      template_name = 'blogs/blog2.html',
      context_object_name = 'Posts',
      paginate_by = 5)
      , name='blog'),
   path('<int:pk>/', views.post, name='post'),
]
