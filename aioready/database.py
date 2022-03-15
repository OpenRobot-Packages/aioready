import asyncio
from dataclasses import MISSING

from typing import Any, Optional, List, Dict

import asyncpg
import asqlite
import aiomysql

import motor.motor_asyncio as motor

from .errors import *
from .utils import URL, parse, copy_docs
from .database_enum import DatabaseType

class Database:
	def __init__(self, type: DatabaseType, url: str = MISSING) -> None:
		self.url = url
		self.type = type

class Connection:
	def __init__(self, *databases: List[Database]) -> None:
		self._databases: List[Database] = databases
		self.databases: Dict[int, Database] = {}

	async def connect(self):
		for index, db in enumerate(iterable=self._databases):
			if db.type == DatabaseType.mongo:
				self.databases[index] = (motor.AsyncIOMotorClient(db.url))
			if db.type == DatabaseType.postgresql:
				self.databases[index] = await (asyncpg.create_pool(db.url))