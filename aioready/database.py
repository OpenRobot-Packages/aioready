try:
	import asyncpg, asqlite, motor.motor_asyncio, aiomysql
except ImportError as e:
	raise ImportError(e) from e
from .utils import parse, URL
import motor.motor_asyncio as aiomongo
import asyncio

# TODO: finish `Connector` class

class Connector:
	def __init__(self, url_or_dsn : str) -> None:
		self._url = url_or_dsn
		self._db = None
		if self.url.scheme == "mongodb":
			self._db = aiomongo.AsyncIOMotorClient(self._url)
		elif self.url.scheme in ("postgre", "postgresql"):
			self._db = asyncpg.create_pool(self._url)

	def init(self):
		if not self._db:
			raise RuntimeError("You do not have a correct connection url or it is not yet implemented.")

	@property
	def url(self) -> URL:
		return self._url

class Database(Connector):
	def __init__(self, url_or_dsn : str) -> None:
		super().__init__(url_or_dsn)
