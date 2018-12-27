from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'accounts/',include('accounts.urls',namespace='accounts')),
    url(r'accounts/',include('django.contrib.auth.urls')),
]
