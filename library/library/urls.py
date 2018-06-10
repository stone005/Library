from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/catalog/')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]