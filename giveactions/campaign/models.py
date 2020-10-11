from django.db import models

#models file, contains classes, which creates the table in the database

#Tag Model, contains :
#   a short name
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#Tag Model, contains :
#   a short title
#   a description
#   an URL image
#   a list of Tag -> can be embty, by default is empty
class Campaign(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    image = models.URLField()
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.title

