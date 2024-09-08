
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from pages import views as ordem_servico_views  # Importa as views do aplicativo ordem_servico
from pages import views
from django.contrib import admin  # Importa o módulo admin

urlpatterns = [
    path('', views.home, name='home'),
    
    #path('logout', views.logout, name='logout'), 
    path('principal', views.principal, name='principal'),
    path('profile', views.profile, name='profile'),
    #path('login', views.login, name='login'), 
    path('proposta', views.proposta, name='proposta'),

    #path('', RedirectView.as_view(pattern_name='criar_ordem_servico'), name='index'),
    path('ordem_servico_registro', views.criar_ordem_servico, name='ordem_servico_registro'),
    path('admin/', admin.site.urls),  # Adiciona as URLs do painel de administração
    path('ordem_servico_confirmacao/', views.ordem_servico_confirmacao, name='ordem_servico_confirmacao'),
    path('emitir_planilha/<int:mes>/<int:ano>/', views.emitir_planilha, name='emitir_planilha'),
    path('historico_ordem_servico/', views.historico_ordem_servico, name='historico_ordem_servico'),
    path('historico_ordem_servico/<int:mes>/', views.historico_ordem_servico, name='historico_ordem_servico'),
    path('baixar_excel/<int:mes>/', views.baixar_excel, name='baixar_excel'),
    
]