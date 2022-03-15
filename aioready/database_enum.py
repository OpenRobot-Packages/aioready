from enum import Enum

class DatabaseType(Enum):
	mongo: str = "mongodb"
	sqlite: str = "sqlite"
	mysql: str = "mysql"
	postgresql: str = "postgresql"