from django.contrib import admin

# Register your models here.
from page.models import Host


@admin.register(Host)
class Host(admin.ModelAdmin):
    list_display = ('host_id', 'host_name', 'applicant', 'host_domain')
    list_per_page = 10
    ordering = ('host_id',)
    search_fields = ('host_name',)  # 搜索字段


class Rule(admin.ModelAdmin):
    list_display = ('IMPLEMENTED', 'CHECK_TYPE', 'rule_id', 'standard','rule_doc_id','title','implemented','level',
                    'type','difficulty','description','check_method','pass_condition')
    list_per_page = 10
    ordering = ('rule_id',)
    search_fields = ('title',)  # 搜索字段


admin.site.site_header = '网站无障碍学习系统后台管理'
admin.site.site_title = '网站无障碍学习系统后台管理'
