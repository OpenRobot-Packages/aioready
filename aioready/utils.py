import typing, urllib

class URL:
	def __init__(self, scheme : str, host : str, port : int) -> None:
		self.scheme = scheme
		self.host = host
		self.port = port

def parse(url : str):
	res = urllib.parse.urlparse(url)
	return URL(res.scheme, res.host, res.port)

def copy_docs(from_obj : typing.Any, to : typing.Any = None):
	def wrapper(f):
		if not to:
			f.__doc__ = from_obj.__doc__
		else:
			to.__doc__ = from_obj.__doc__
	return wrapper