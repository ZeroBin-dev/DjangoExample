from django.contrib import admin
from django.urls import path
from myapp.views import hello  # 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),  # 추가
]
