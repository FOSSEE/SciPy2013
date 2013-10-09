from django.db import models
from django.contrib.auth.models import User

def get_document_dir(instance, filename):
    return '%s/document/%s' % (instance.user, filename)

def get_presentation_dir(instance, filename):
    return '%s/presentation/%s' % (instance.user, filename)

class Paper(models.Model):
    user = models.ForeignKey(User)
    document = models.FileField(upload_to=get_document_dir)
    verified = models.NullBooleanField()
