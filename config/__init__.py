from fastapi import FastAPI
from databases import Database
import sqlalchemy

app = FastAPI(
    title="marketplace-v1",
    debug=True
)

""" DATABASE CONNECTION """


DATABASE_URL = ""
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)


""" APP EVENT SETTING """


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
