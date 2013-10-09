from django.contrib import admin

from website.models import Paper

class PaperAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified')

admin.site.register(Paper, PaperAdmin)

