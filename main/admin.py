from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Member


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'title_length',
        'contents',
        'writer',
        'created',
        'photo_tag'
        )

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px;" />')
        return None

    # list_display_links = (
    #     'title',
    # )

    search_fields = (
        'title',
        'contents',
    )

    list_filter = (
        'title',
        'contents',
    )

    def title_length(self, post):
        return len(post.title) #  연습용


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        # 'loginId',
        'loginPw',
        'email',
    )


# class ReviewAdmin(admin.ModelAdmin):
#     list_display = (
#         'comment',
#     )


admin.site.register(Post, PostAdmin)
admin.site.register(Member, MemberAdmin)
# admin.site.register(Review, MemberAdmin)