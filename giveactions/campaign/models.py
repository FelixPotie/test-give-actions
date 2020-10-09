from django.db import models


class Tag(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Campaign(models.Model):
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    image = models.URLField()
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.titre

