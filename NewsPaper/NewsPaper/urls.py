
from django.contrib import admin
from django.urls import path, include
from news.views import subscriptions


urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path("authors/", include("allauth.urls")),
   path('news/', include('news.urls')),
   path('subscriptions/', subscriptions, name='subscriptions'),
]
