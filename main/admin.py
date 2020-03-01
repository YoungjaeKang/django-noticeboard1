from django.contrib import admin
from .models import Post, Member


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'contents',
        'writer',
        'created',
        )


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        # 'loginId',
        'loginPw',
        'email',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Member, MemberAdmin)