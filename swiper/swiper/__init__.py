import pymysql
from .my_celery import app as celery_app

__all__ = ('celery_app',)

pymysql.install_as_MySQLdb()