from django.contrib import admin

# Register your models here.

from valorantapp.model import Blog, Weapons, Characters, Skill
admin.site.register(Blog)
admin.site.register(Weapons)
admin.site.register(Characters)
admin.site.register(Skill)

