from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('urugendo.urls')),
    path('api/', include('SmallShop.urls')),
]
