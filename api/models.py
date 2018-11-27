from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Below ___str___ method defines what we get when we ask for a particular instance of model
# Meaning this would get back only the title from the model

    def __str__(self):
        return '%s %s' % (self.title, self.body)

# Now including the body field

class BinSchedule(models.Model):
    bintype = models.CharField(max_length=200)
    date =  models.CharField(max_length=200)
    council = models.CharField(max_length=200)


    def __str__(self):
        return '%s %s %s' % (self.bintype, self.date, self.council)

