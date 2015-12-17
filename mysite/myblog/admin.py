from django.contrib import admin

# Register your models here.
from .models import MyUser, Tag, Entity, Review, Vote, Criteria_Teacher, Criteria_Uni

admin.site.register(MyUser)
admin.site.register(Tag)
admin.site.register(Entity)
admin.site.register(Review)
admin.site.register(Vote)
admin.site.register(Criteria_Teacher)
admin.site.register(Criteria_Uni)
