from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content_size','status', 'created_at','updated_at']

    actions = ['make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'


    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published 상태로 변경합니다.'


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class Tagadmin(admin.ModelAdmin):
    list_display = ['name']

