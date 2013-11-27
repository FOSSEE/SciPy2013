from django.db import models
from django.contrib.auth.models import User

def get_document_dir(instance, filename):
    return '%s/document/%s' % (instance.user, filename)

def get_presentation_dir(instance, filename):
    return '%s/presentation/%s' % (instance.user, filename)

class Paper(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    affiliation = models.CharField(max_length=250)
    objective = models.CharField(max_length=512)
    abstract = models.TextField(max_length=700)
    bio = models.TextField(max_length=500)
    links = models.CharField(max_length=128)
    attachments = models.FileField(upload_to=get_document_dir)
    verified = models.NullBooleanField()

class Comment(models.Model):
    paper = models.ForeignKey(Paper)
    comment_by = models.ForeignKey(User)
    comment = models.CharField(max_length=500)

