from peewee import AutoField, CharField
import numpy as np

from ai.landmark_detection.domain.Entity import Entity


class Descriptor(Entity):
    descriptor_id = AutoField()
    feature40 = CharField(max_length=1023)

    def feature40_np(self):
        return np.array([float(feature) for feature in str(self.feature40).split(',')])
