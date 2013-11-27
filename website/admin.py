from django.contrib import admin

from website.models import Paper, Comment

class PaperAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'comment_by')

admin.site.register(Paper, PaperAdmin)
admin.site.register(Comment, CommentAdmin)

