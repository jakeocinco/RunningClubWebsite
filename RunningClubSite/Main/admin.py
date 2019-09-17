from django.contrib import admin
from .models import Post
from .models import Meet
from .models import FAQ
from .models import Executives

# Register your models here.
admin.site.register(Post)

admin.site.register(Meet)

admin.site.register(FAQ)

admin.site.register(Executives)
