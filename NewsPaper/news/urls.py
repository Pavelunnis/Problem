from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostSearch, PostUpdate, PostDelete, subscriptions
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', (cache_page(60))(NewsList.as_view()), name='post_list'),
   path('<int:pk>', (cache_page(300))(NewsDetail.as_view()), name='news_detail'),
   path('create/', (cache_page(60))(PostCreate.as_view()), name='post_create'),
   path('articles/create/', PostCreate.as_view(), name='post_create'),
   path('search/',PostSearch.as_view(), name='search'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]