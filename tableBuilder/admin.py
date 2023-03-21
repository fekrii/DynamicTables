from django.contrib import admin
from .models import TableNames, TableSchema, TableFieldSchema

admin.site.register(TableNames)
admin.site.register(TableSchema)
admin.site.register(TableFieldSchema)


models = TableNames.objects.all()
for model in models:
    reg_model = TableSchema.objects.get(name=model.tablename).as_model()
    admin.site.register(reg_model)
