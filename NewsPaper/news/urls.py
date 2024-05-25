from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostSearch, PostUpdate, PostDelete, subscriptions

urlpatterns = [
   path('', NewsList.as_view(), name='post_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('articles/create/', PostCreate.as_view(), name='post_create'),
   path('search/',PostSearch.as_view(), name='search'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]