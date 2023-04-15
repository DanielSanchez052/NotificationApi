from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(
        'created at', auto_now_add=True, auto_now=False)
    modified_at = models.DateField(
        'modified at', auto_now_add=False, auto_now=True)
    deleted_at = models.DateField(
        'deleted at', auto_now_add=False, auto_now=True)


    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Model'
