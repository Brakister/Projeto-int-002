from django.contrib import admin

from .models import Loja
from .models import Servico
from .models import OrdemServico
admin.site.register(Loja)# Registra o modelo Loja no painel de administração
admin.site.register(Servico)# Registra o modelo Servico no painel de administração
admin.register(OrdemServico)# Registra o modelo OrdemServico no painel de administração
