from django.contrib import admin

from deploy_test.models import Picture


class PictureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Picture, PictureAdmin)
