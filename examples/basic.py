from aioready import Database, DatabaseType, Connection
import asyncio

db = Database(DatabaseType.postgresql, "db")

con = Connection(db)

asyncio.run(con.connect())

print(con.databases) # gives out the databases