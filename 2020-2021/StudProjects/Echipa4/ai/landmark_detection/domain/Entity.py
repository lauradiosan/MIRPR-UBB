from peewee import Model
from playhouse.pool import PooledSqliteDatabase

from ai.landmark_detection.environment import DB_PATH

sqlite_db = PooledSqliteDatabase(
    DB_PATH,
    max_connections=32,
    stale_timeout=300
)


class Entity(Model):
    class Meta:
        database = sqlite_db
