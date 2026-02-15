from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'due_date', 'completed', 'created_at')
    list_filter = ('completed', 'category', 'due_date')
    search_fields = ('title', 'category__name')
    ordering = ('-created_at',)
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'category', 'due_date')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
