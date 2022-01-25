from django.db import models


class region (models.Model):
    Name = models.CharField(max_length=12) 

def __all__(self):  
    return self.regiao

class fruit(models.Model):
    Name = models.CharField(max_length=12)  
    regfruit = models.ForeignKey(region, on_delete=models.CASCADE)

def __all__(self):
        return self.fruta  
        