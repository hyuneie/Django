from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
    path('sport', views.sport, name='sport'),
    path('minwon', views.minwon, name='minwon'),
    path('test', views.getTestDatas, name="blogdatas"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)