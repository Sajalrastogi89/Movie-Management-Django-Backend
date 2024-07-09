from django.contrib import admin
from django.urls import path, include
from .views import dummy_view  # Import the dummy view function

urlpatterns = [
    path('', dummy_view),  # Root URL that returns a dummy string
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
]
