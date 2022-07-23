"""
Day 49: Create a Database
For this challenge, you are going to create a database using Python’s SQLite. You will
import SQLite into your script. Create a database called movies.db. In that database,
you are going to create a table called movies. In that table, you are going to save
the following movies:
year title      genre
2009 Brothers   Drama 
2002 Spider Man Sci-fi
2009 WatchMen   Drama
2010 Inception  Sci-fi
2009 Avatar  Fantasy
genre
Drama Sci-fi Drama Sci-fi Fantasy
 a) Once you create a table, run a SQL query to see all the movies in your table.
b) Run another SQL query to select only the movie Brothers from the list.
c) Run another SQL query to select all movies that were released in 2009 from your table.
d) Run another query to select movies in the fantasy and drama genre.
e) Run a query to delete all the contents of your table.
"""
import sqlite3 as db

def createConnection(nameOfDb):
    try:
      return db.connect(nameOfDb)
    except:
        print("connection exeption occured")
    

def createTable(getConnection):
    print('\n\nCreating table...')
    #create table
    createTablequery = """CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER(4),
    title VARCHAR(20),
    genre VARCHAR(15)
    );
    """
    getCursor = getConnection.cursor()

    #execute create query
    getCursor.execute(createTablequery)
    print('Table creation successfull...\n\n')

#show tables
def getAllTables(getConnection):
    print(getConnection.cursor().execute("""SELECT name FROM sqlite_master
        WHERE type='table'""").fetchall())

def insertToMovies(getConnection):
    print("\n\ninserting data into table...")
    insertQuery = """
    INSERT INTO movies(year, title, genre)
    values(?, ?, ?);"""
    listOfMovies = [(2009, 'Brothers', 'Drama'), (2002, 'Spider Man', 'Sci-fi'),
        (2009, 'WatchMen', 'Drama'),(2010, 'Inception', 'Sci-fi'), 
        (2009, 'Avatar', 'Fantasy')]

    # execute insert query 
    getConnection.cursor().executemany(insertQuery,listOfMovies)
    getConnection.commit() # commit to dabase;
    print('insertion data complete to the data base......')

def fetchAllRecordFromMovies(getConnection:db.Connection):
    return getConnection.cursor().execute("select * from movies").fetchall()


def fetchMoviesByTitle(getConnection:db.Connection, title):
   
    return getConnection.cursor().execute(f"""select * from movies m
     where m.title='{title}'""").fetchall()


def fetchMoviesByGenre(getConnection: db.Connection, genre):

    return getConnection.cursor().execute(f"""select * from movies m
     where m.genre='{genre}'""").fetchall()

def truncateTable(getConnection: db.Connection, tableName):
    try:
        print(f'\n\nDeleting all data from table{tableName}...')
        query = f"delete from {tableName};"
        print(query)
        getConnection.cursor().execute(query)
        print(f'Deleting data from {tableName} completed...')
    except:
        print(f'removing data from {tableName} isn\'t successful.')

#execute all above fnction from main
if __name__ == "__main__":
    dbName = "movies.db"
    getConnection = createConnection(dbName)
    createTable(getConnection) 
    # getAllTables(getConnection)
    insertToMovies(getConnection) #--> uncomment it only once otherwise same record will be inserted
    print(fetchAllRecordFromMovies(getConnection))
    print(fetchMoviesByTitle(getConnection,'Brothers'))
    print(fetchMoviesByGenre(getConnection,'Fantasy'))
    truncateTable(getConnection, 'movies')


