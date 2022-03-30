from django.db import models
  
class BBModel(models.Model):
 
    # fields of the model
    tanggal = models.DateTimeField(blank=True, null=True)
    bb_min = models.IntegerField()
    bb_max = models.IntegerField()
    
    class Meta:
        db_table = 'bb_model'

    # with their title name
    def __str__(self):
        return self.tanggal
