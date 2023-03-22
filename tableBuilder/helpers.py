from django.db import connections, models

class ModelSchema:
    

    
    def __init__(self, model_name, fields=None):
        self.model_name = model_name
        self.fields = fields
        
    
    def make_model(self):
        model = type(
            self.model_name,
            (models.Model,),
            self.get_attr()
        )
        
        return model
        
    def get_attr(self):
        
        DATA_TYPES = {
            'string': models.CharField(max_length=255),
            'number': models.IntegerField(),
            'boolean': models.BooleanField()
        }
        
        attrs = {
            # field : models.CharField(max_length=255),
            "Meta": type(
                "Meta",
                (),
                {"app_label": "tableBuilder"}
            ),
            '__module__': 'tableBuilder.models'
        }
        if self.fields:
            for field in self.fields:
                attrs[field["title"]] = DATA_TYPES[field["type"]]
        return attrs
    
