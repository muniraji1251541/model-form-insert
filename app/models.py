from django.db import models

# Create your models here.


class Topic(models.Model):
    toipc_name=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.toipc_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()

    def __str__(self):
        return self.name

class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()