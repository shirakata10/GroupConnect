from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('bordlist', views.BordlistView.as_view(), name='bordlist'),
    path('bord', views.BordView.as_view(), name='bord'),
    path('notfound', views.NotFoundView.as_view(), name='notfound'),
]