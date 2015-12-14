from django.contrib import admin

# Register your models here.
from .models import MyUser, Tag, Entity, Review, Vote

admin.site.register(MyUser)
admin.site.register(Tag)
admin.site.register(Entity)
admin.site.register(Review)
admin.site.register(Vote)
