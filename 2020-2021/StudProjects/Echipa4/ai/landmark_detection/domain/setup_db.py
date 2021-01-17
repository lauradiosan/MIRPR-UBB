from ai.landmark_detection.domain.Descriptor import Descriptor
from ai.landmark_detection.domain.Entity import sqlite_db
from ai.landmark_detection.domain.Landmark import Landmark
from ai.landmark_detection.domain.Location import Location

if __name__ == '__main__':
    sqlite_db.connect()
    sqlite_db.create_tables(
        [Landmark, Location, Descriptor]
    )
