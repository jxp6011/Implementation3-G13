from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import User, Post, Comment, Like

# Register your models here.




class UserInline(admin.StackedInline):
    model = User.following.through
    fk_name = 'to_user'
    verbose_name = 'Follower'
    verbose_name_plural = 'Followers'

class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(GenericStackedInline):
    model = Like

UserAdmin.fieldsets += (('Custum fields', {'fields': ('profile_pic', 'nickname', 'whatsapp_id', 'address', 'latitude', 'longitude', 'following',)}),)
UserAdmin.inlines = (
    UserInline,
)

class PostAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
        LikeInline,    
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInline,
    )


admin.site.register(User, UserAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Like)