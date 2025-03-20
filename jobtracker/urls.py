from django.contrib import admin
from django.urls import path, include
from jobtracker.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    #path('applications/', include('applications.urls')),
]