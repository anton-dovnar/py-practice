import sqlite3


class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()


class Movie:
    table = 'Movie'  # Table
    key = 'title'  # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key


class Song:
    table = 'Music'  # Table
    key = 'title'  # Primary key
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key


if __name__ == "__main__":
    with sqlite3.connect('entertainment.db') as conn:
        c = conn.cursor()

        # If table does not exist then create one
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Movie'")
        if c.fetchone()[0] != 1:
            c.execute("CREATE TABLE Movie (title, director, year)")
            c.execute("INSERT INTO Movie VALUES ('Star Wars','George Lucas','1977')")
            conn.commit()
        print(Movie('Star Wars').director)
        Movie('Star Wars').director = 'J.J. Abrams'  # Set another director
        print(Movie('Star Wars').director)

        # If table does not exist then create one
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Music'")
        if c.fetchone()[0] != 1:
            c.execute("CREATE TABLE Music (title, artist, year, genre)")
            c.execute("INSERT INTO Music VALUES ('Take Me Home, Country Roads','John Denver','1971','Country')")
            conn.commit()
        print(Song('Take Me Home, Country Roads').artist)
