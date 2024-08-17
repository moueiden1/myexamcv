import os 
import sys
from math import sqrt, log, e
from random import choice, random

__author__ = 'Oueideng Modeste; Data Analysis'
__license__ = 'BSD 3 Simplified'
__version__ = '0.1.0'
__email__ = 'weideng@gmail.com'

module_level_variable1 = 12345

module_level_variable2 = 98765

import oauth2

API_KEY = '5Hqg6JTZ0cC89hUThySd5yZcL'
API_SECRET = 'Ncp1oi5tUPbZF19Vdp8Jp8pNHBBfPdXGFtXqoKd6Cqn87xRj0c'
TOKEN_KEY = '3272304896-ZTGUZZ6QsYKtZqXAVMLaJzR8qjrPW22iiu9ko4w'
TOKEN_SECRET = 'nsNY13aPGWdm2QcgOl0qwqs5bwLBZ1iUVS2OE34QsuR4C'


def oauth_req(url, key, secret, http_method="GET", post_body="",
    http_headers=None):
    consumer = oauth2.Consumer(key=API_KEY, secret=API_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method,
    body=post_body, headers=http_headers)
    return content


url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor'
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)

with open("../../data/chp13/hashchildlabor.json", "w") as data_file:
    data_file.write(data)
