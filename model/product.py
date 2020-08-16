import sqlalchemy
from config import metadata
from datetime import datetime

""" Model to Product"""
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("sku", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("referenceSku", sqlalchemy.Text, unique=True),
    sqlalchemy.Column("name", sqlalchemy.Text),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("shortDescription", sqlalchemy.Text),
    sqlalchemy.Column("brand", sqlalchemy.Text),
    sqlalchemy.Column("status", sqlalchemy.Boolean),
    sqlalchemy.Column("ean", sqlalchemy.String(14), unique=True),
    sqlalchemy.Column("keyWords", sqlalchemy.ARRAY(sqlalchemy.String())),
    sqlalchemy.Column("createdAt", sqlalchemy.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S")),
    sqlalchemy.Column("updatedAt", sqlalchemy.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S"))
)