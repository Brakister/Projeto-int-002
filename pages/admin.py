from django.contrib import admin

from .models import Loja
from .models import Servico
from .models import OrdemServico
admin.site.register(Loja)
admin.site.register(Servico)
admin.register(OrdemServico)
