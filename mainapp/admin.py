from django.contrib import admin
from django.utils.html import format_html

from mainapp.models import News, Course, Lesson, CourseTeacher


admin.site.register(Course)
admin.site.register(CourseTeacher)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'deleted')
    list_filter = ('deleted', 'created_at')
    ordering = ('pk',)
    list_per_page = 5
    search_fields = ('title', 'preamble', 'body',)
    actions = ('mark_as_delete',)

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            obj.title.lower().replace(' ', '-'),
            obj.title
        )

    slug.short_description = 'Слаг'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'deleted')
    list_filter = ('course', 'deleted', 'created_at')
    list_per_page = 5

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = ('Course')

    search_fields = ('course', 'title', )
    actions = ('mark_as_delete',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'

