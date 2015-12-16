# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from os import environ
import sys
import json

conf = {}
with open("{}/.robofriend.json".format(environ.get("HOME"))) as f:
    conf = json.load(f)

base = conf.get('base', '')
app = sys.argv[1]
_from = conf.get('numbers', {}).get(sys.argv[2])
_to = conf.get('numbers', {}).get(sys.argv[3])

client = TwilioRestClient()

call = client.calls.create(url="{}/{}.xml".format(base, app),
    method='GET',
    to=_to,
    from_=_from,
)
