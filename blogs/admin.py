from django.contrib import admin
from .models import blogs, comment, author

admin.site.register(author)
admin.site.register(comment)

class blogcommentsinline(admin.TabularInline):
    model = comment
    max_num = 0

@admin.register(blogs)
class blogadmin(admin.ModelAdmin):
    list_display = ('btitle','user','bdate')
    inlines = [blogcommentsinline]
