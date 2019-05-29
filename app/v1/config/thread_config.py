import requests
# from datetime import datetime, timedelta
import json

POOL_TIME = 60

ACTION = 'get_events'
API_KEY = '61f3a93fc374f91735aaa1b385c8427ab11e838206653f45db75a7c733ed1dc7'


def fetch3rdAPI(league_id):

    # today = datetime.now()
    # from_date = today - timedelta(days=3)
    # to_date = today + timedelta(days=8)
    #
    # from_date_str = from_date.strftime('%y-%m-%d')
    # to_date_str = to_date.strftime('%y-%m-%d')

    from_date_str = '19-05-10'
    to_date_str = '19-05-17'

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

