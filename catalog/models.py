from django.db import models

# Create your models here.
class FederalSupplyClassification(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'federal_supply_classification'
    
    

class FederalSupplyGroup(models.Model):
    class Meta:
        db_table = 'federal_supply_group'

    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    

