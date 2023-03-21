from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TableNames, TableFieldSchema, TableSchema
from .helpers import ModelSchema
from django.db import connection
from django.contrib import admin
from importlib import import_module,reload
from django.conf import settings
from django.urls import clear_url_caches
from django.http import HttpResponseBadRequest
from django.core.serializers import serialize
from django.http import HttpResponse     


 
class CreateTableView(APIView):
    def get(self, request):
        return Response("GET")
    def post(self, request):
        
        # Get data from request
        table_name = request.data['table_name']
        table_fields = request.data['fields']
        
        ## TODO: add transaction atomic
        
        ## create Table
        table = TableSchema.objects.create(name=table_name)
        
        ## add table name to TableNames
        TableNames.objects.create(tablename=table_name)
        
        ## add Table Fields
        for field in table_fields:
            TableFieldSchema.objects.create(table_schema=table, name=field["title"], field_type=field["type"])
        
        ## create dynamic model with ModelSchema
        schema = ModelSchema(table_name, table_fields)
        model = schema.make_model()
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(model)
            admin.site.register(model)
            reload(import_module(settings.ROOT_URLCONF))
            clear_url_caches()
        return Response("POST")
    
    
class TableUpdateView(APIView):
        
    def put(self, request, name):
        # Get data from request
        table_name = request.data['table_name']
        table_fields = request.data['fields']
        
        ## update dynamic model with ModelSchema
        schema = ModelSchema(table_name, table_fields)
        model = schema.make_model()
        with connection.schema_editor() as schema_editor:
            schema_editor.remove_field(model, "name")
            # admin.site.register(model)
            # reload(import_module(settings.ROOT_URLCONF))
            # clear_url_caches()
        return Response("PUT")
    


class TableRowView(APIView):
    ## TODO: add set up function 
    def get(self, request, name):
            
        # get data from request
        data = request.data
        

        # get table 
        try:
            table = TableSchema.objects.get(name=name)
        except:
            return HttpResponseBadRequest('Table Not Found', status=400)
        
        
        # get table fields
        fields_objects = TableFieldSchema.objects.filter(table_schema=table)
        fields = []
        for field in fields_objects:
            fields.append({
                "title" : field.name,
                "type": field.field_type
            })

        schema = ModelSchema(table.name, fields)
        model = schema.make_model()
        data = model.objects.all()


        data = serialize("json", data, fields=tuple(value['title'] for value in fields))
        return HttpResponse(data, content_type="application/json")
    def post(self, request, name):
            
        # get data from request
        data = request.data
        

        # get table 
        try:
            table = TableSchema.objects.get(name=name)
        except:
            return HttpResponseBadRequest('Table Not Found', status=400)
        
        
        # get table fields
        fields_objects = TableFieldSchema.objects.filter(table_schema=table)
        fields = []
        for field in fields_objects:
            fields.append({
                "title" : field.name,
                "type": field.field_type
            })
        
        schema = ModelSchema(table.name, fields)
        model = schema.make_model()
        try:
            model.objects.create(**data)
        except:
            return HttpResponseBadRequest('Object NOt created', status=400)
        return Response("ADD DATA POST")
