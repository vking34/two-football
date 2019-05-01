import requests
from datetime import datetime, timedelta
import json

POOL_TIME = 5

ACTION = 'get_events'
LEAGUE_ID = 63
API_KEY = 'ac2f0ea7166d4eb7ce9da12cfe706295023ba68ee9a060f3f4928709d4ef68e0'


def fetch3rdAPI():

    today = datetime.now()
    from_date = today - timedelta(days=1)
    to_date = today + timedelta(days=6)

    from_date_str = from_date.strftime('%y-%m-%d')
    to_date_str = to_date.strftime('%y-%m-%d')

    params = (('action', ACTION),
              ('from', from_date_str),
              ('to', to_date_str),
              ('league_id', LEAGUE_ID),
              ('APIkey', API_KEY))

    content = requests.get('https://apifootball.com/api/', params=params).content
    match_list = json.loads(content.decode('utf8'))

    return match_list

