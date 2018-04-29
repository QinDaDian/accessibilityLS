from django.contrib import admin

# Register your models here.
from page.models import Host,Rule,Page


@admin.register(Host)
class Host(admin.ModelAdmin):
    list_display = ('host_id', 'host_name', 'host_domain')
    list_per_page = 10
    ordering = ('host_id',)
    search_fields = ('host_name',)  # 搜索字段



@admin.register(Rule)
class Rule(admin.ModelAdmin):
    list_display = ('IMPLEMENTED', 'CHECK_TYPE', 'rule_id', 'standard', 'rule_doc_id', 'title', 'implemented', 'level',
                    'type', 'difficulty', 'description', 'check_method', 'pass_condition', 'freq_ans')
    list_per_page = 10
    ordering = ('rule_id',)
    search_fields = ('title',)  # 搜索字段


@admin.register(Page)
class Page(admin.ModelAdmin):
    list_per_page = 10
    ordering = ('page_id',)
    search_fields = ('title',)


admin.site.site_header = '网站无障碍学习系统后台管理'
admin.site.site_title = '网站无障碍学习系统后台管理'
