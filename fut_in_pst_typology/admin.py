from django.contrib import admin

from .models.language import Language
from .models.genus import Genus
from .models.family import Family


admin.site.register(Language)
admin.site.register(Genus)
admin.site.register(Family)