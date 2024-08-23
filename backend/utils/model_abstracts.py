import uuid
from django.db import models

#every model in django has to inerit models.models
class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True