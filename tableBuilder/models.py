from django.db import models
from django.apps import apps
from .helpers import ModelSchema
from django.db import connection


class TableNames(models.Model):
    tablename = models.CharField(max_length=100)

    def __str__(self):
        return self.tablename


class TableSchema(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def as_model(self):
        # get fields
        fields_objects = TableFieldSchema.objects.filter(table_schema__name=self.name)
        fields = []
        for field in fields_objects:
            fields.append({
                "title" : field.name,
                "type": field.field_type
            })
        try:
            return apps.get_model("tableBuilder", self.name)
        except:
            schema = ModelSchema(self.name, fields)
            model = schema.make_model()
            with connection.schema_editor() as schema_editor:
                schema_editor.alter_db_table(model, self.name, self.name)
            return model
        
    def __str__(self):
        return self.name


class TableFieldSchema(models.Model):
    
    DATA_TYPES = {
        'string': models.CharField,
        'number': models.IntegerField,
        'boolean': models.BooleanField
    }
    
    name = models.CharField(max_length=100)
    table_schema = models.ForeignKey(
        TableSchema,
        on_delete=models.CASCADE,
        related_name='table_fields'
    )
    field_type = models.CharField(
        max_length=16,
        choices=[(dt, dt) for dt in DATA_TYPES]
    )
    
    def __str__(self):
        return self.name