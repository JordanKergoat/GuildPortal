__author__ = 'Alexandre Cloquet'

import requests

r = requests.get('https://api.twitch.tv/kraken/streams/nkio_',
                 headers={'Accept': 'application/vnd.twitchtv.v3+json'})

print(r.status_code)
print(r.json())
