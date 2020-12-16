import kwargs as kwargs
from django.db import models

# Create your models here.
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Link(DjangoCassandraModel):
    #link_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    url = columns.Text(required=True,primary_key=True)
    list_users = columns.List(columns.Text)
    created = columns.DateTime()
