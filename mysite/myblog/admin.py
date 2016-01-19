from django.contrib import admin

# Register your models here.
from .models import MyUser, Tag, Entity, Review, Vote, Criteria_Teacher, Criteria_Uni, Subject, Criteria_Optional
from .models import Entity_Edit_Info, Entity_Add_Info

admin.site.register(MyUser)
admin.site.register(Tag)
admin.site.register(Entity)
admin.site.register(Review)
admin.site.register(Vote)
admin.site.register(Criteria_Teacher)
admin.site.register(Criteria_Uni)
admin.site.register(Criteria_Optional)
admin.site.register(Subject)
admin.site.register(Entity_Edit_Info)
admin.site.register(Entity_Add_Info)
