from peewee import AutoField, FloatField, CharField
import numpy as np

from ai.landmark_detection.domain.Entity import Entity


class Location(Entity):
    location_id = AutoField()
    y = FloatField()
    x = FloatField()
    yx_pair = CharField(unique=True)

    def location_np(self):
        """
            [0] - vertical
            [1] - horizontal
        :return: np array
        """
        return np.array([self.y, self.x])
