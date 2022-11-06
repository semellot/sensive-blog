from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'author')
    raw_id_fields = ['author', 'likes']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('published_at', 'post', 'author', 'text')
    raw_id_fields = ['post', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
