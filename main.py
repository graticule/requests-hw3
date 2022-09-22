import requests
import datetime
import time
from pprint import pprint


def unix_timestamp_from_datetime(d: datetime.datetime):
    return int(time.mktime(d.timetuple()))


if __name__ == '__main__':
    url = 'https://api.stackexchange.com/2.3/questions'
    today = unix_timestamp_from_datetime(datetime.datetime.now())
    two_day_ago = unix_timestamp_from_datetime(datetime.datetime.now() - datetime.timedelta(days=2))
    params = {'fromdate': two_day_ago,
              'todate': today,
              'order': 'desc',
              'sort': 'creation',
              'tagged': 'python',
              'site': 'stackoverflow'}
    response = requests.get(url=url, params=params)
    pprint(response.json()['items'])