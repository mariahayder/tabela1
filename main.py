import sqlite3
from fastapi import FastAPI, Query

{
        "TrackId": int,
        "Name": str,
        "AlbumId": int,
        "MediaTypeId": int,
        "GenreId": int,
        "Composer": str,
        "Milliseconds": int,
        "Bytes": int,
        "UnitPrice": float
}

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect('chinook.db')


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/tracks/{page}/{per_page}")
async def root(page: int = 0, per_page: int = 10):
    cursor = app.db_connection.cursor()
    print("page: "+page+"per_page: "+per_page)
    offset=page*per_page
    data = app.db_connection.execute("SELECT * FROM tracks ORDER BY TrackId LIMIT %d OFFSET %d" % (per_page, offset)).fetchall()
    return data

