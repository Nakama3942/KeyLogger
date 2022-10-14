import datetime


def calendar(not_ms: bool = True) -> datetime:
	if not_ms:
		return datetime.datetime.today().replace(microsecond=0)
	return datetime.datetime.today()
