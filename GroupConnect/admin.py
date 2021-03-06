from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import User, Group, Member, Signboard, Post, Situation,Category,GroupIcon

class GroupIconAdmin(admin.ModelAdmin):
    pass

admin.site.register(GroupIcon)

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)


class SituationAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'user_id', 'read_situation')

admin.site.register(Situation, SituationAdmin)

class SituationInline(admin.TabularInline):
    model = Situation
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'signboard_id', 'text', 'contributer', 'created_at', 'read_number')
    inlines = [SituationInline]

admin.site.register(Post, PostAdmin)

class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_id', 'name')

admin.site.register(Category, CategoryAdmin)


class SignboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_id', 'title', 'category_id', 'text', 'updated_at')
    inlines = [PostInline]

admin.site.register(Signboard, SignboardAdmin)

class SignboardInline(admin.TabularInline):
    model = Signboard
    extra = 0


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'group_id', 'name', 'authority')

admin.site.register(Member, MemberAdmin)

class MemberInline(admin.TabularInline):
    model = Member
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 'icon', 'created_at')
    inlines = [SignboardInline, MemberInline]

admin.site.register(Group, GroupAdmin)
