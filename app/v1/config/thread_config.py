import requests
from datetime import datetime, timedelta
import json

POOL_TIME = 15

ACTION = 'get_events'
API_KEY = 'ac2f0ea7166d4eb7ce9da12cfe706295023ba68ee9a060f3f4928709d4ef68e0'


def fetch3rdAPI(league_id):

    today = datetime.now()
    from_date = today - timedelta(days=3)
    to_date = today + timedelta(days=8)

    from_date_str = from_date.strftime('%y-%m-%d')
    to_date_str = to_date.strftime('%y-%m-%d')

    params = (('action', ACTION),
              ('from', from_date_str),
              ('to', to_date_str),
              ('league_id', league_id),
              ('APIkey', API_KEY))

    # bytes
    content = requests.get('https://apifootball.com/api/', params=params).content

    # list
    match_list = json.loads(content.decode('utf8'))

    # when no events, result is object
    if type(match_list) is not list:
        return None

    return match_list

