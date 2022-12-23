from django.db import models

# Create your models here.
class investors(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class projects(models.Model):
    investor_name=models.ForeignKey(investors,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,null=True)
    share=models.FloatField(null=True,max_length=100)
    def __str__(self):
        return self.name

class payments_tbl(models.Model):
    investor=models.CharField(max_length=100,null=True)
    amount=models.FloatField(null=True,default=0.0)
    date_added=models.DateField(auto_now_add=False,null=True,auto_now=False)
    description=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.investor


class profit_tbl(models.Model):
    projects=models.CharField(max_length=100,null=True)
    amount=models.FloatField(null=True)
    date_added=models.DateField(auto_now_add=False,null=True,auto_now=False)
    def __str__(self):
        return self.projects

