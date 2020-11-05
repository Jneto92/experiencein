from django.urls import path, re_path, include
from perfis import views
from rest_framework.authtoken import views as auth_views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('perfis', views.PerfilViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('perfis/', views.get_meu_perfil, name='perfil'),
	path('convites/', views.get_convites, name="convite"),
	# re_path(r'^perfis/\d+$', views.exibir, name='perfis')
	path('convites/convidar/<int:perfil_id>', views.convidar, name='convidar'),
	path('convites/aceitar/<int:convite_id>', views.aceitar, name='aceitar'),
	path('login/', auth_views.obtain_auth_token, name = 'login')
]