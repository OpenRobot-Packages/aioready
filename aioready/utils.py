import typing, urllib

class URL:
	def __init__(self, scheme : str, host : str, port : int) -> None:
		self.scheme = scheme
		self.host = host
		self.port = port

def parse(url : str):
	res = urllib.parse.urlparse(url)
	return URL(res.scheme, res.host, res.port)