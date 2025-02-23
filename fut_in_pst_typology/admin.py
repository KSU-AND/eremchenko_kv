from django.contrib import admin

from .models.language import Language
from .models.area import Area
from .models.genus import Genus
from .models.family import Family
from .models.comment import Comment
from .models.comment_image import CommentImage
from .models.theory import TheoryBlock 


admin.site.register(Language)
admin.site.register(Area)
admin.site.register(Genus)
admin.site.register(Family)
admin.site.register(Comment)
admin.site.register(CommentImage)
admin.site.register(TheoryBlock)