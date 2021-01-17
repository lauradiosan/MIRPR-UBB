from ai.landmark_detection.domain.Entity import Entity
from peewee import AutoField, CharField, Field


class Landmark(Entity):
    landmark_id = AutoField()
    name = CharField(unique=True)
    wiki_link = CharField()
    location_ids = CharField(max_length=1023)
    descriptor_ids = CharField(max_length=1023)
