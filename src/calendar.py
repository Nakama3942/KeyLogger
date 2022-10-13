import datetime


def calendar() -> datetime:
	return datetime.datetime.today().replace(microsecond=0)
