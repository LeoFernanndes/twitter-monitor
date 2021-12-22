import requests
from decouple import config
import time
from twitter_auth import twitter_authentication
from utils import get_arroba_attributes, validate_arroba
import tweepy


i = 0
while True:
    i += 1
    API_ROOT = config('API_ROOT')
    config_response = requests.get(f'{API_ROOT}/api-config')
    profiles_response = requests.get(f'{API_ROOT}/profiles')
    print(f'{i} iteração')
    print(config_response.content)
    print(profiles_response.content)
    if validate_arroba("@leofernanndes_"):
        print(get_arroba_attributes("@leofernanndes_")._json)
        print('----- PULA LINHA -----')
        print(twitter_authentication().user_timeline(screen_name='@leofernanndes_', include_rts=True,
                                                     tweet_mode='extended')[0]._json)
    time.sleep(60)
