from django.urls import path
from home import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('docreg/', views.docreg, name='docreg'),
    path('doclog/', auth_view.LoginView.as_view(template_name='home/doclog.html'), name='doclog'),
    path('dochome/', views.dochome, name='dochome'),
    path('docout/', auth_view.LogoutView.as_view(template_name='home/docout.html'), name='docout'),
    path('docprof/', views.docprof, name='docprof'),
]