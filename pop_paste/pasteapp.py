#!/usr/bin/python3

"""
pop-paste - A simple CLI Utility to paste text to the Pop_Planet pastebin.

Copyright 2018 Ian Santopietro <isantop@gmail.com>
"""

import json
from urllib import request as req
from urllib import parse

class Paste():
    """The Paste class for Pop Paste."""

    pastebin = 'https://paste.pop-planet.info'
    api_url = '{}/api'.format(pastebin)
    create_url = '{}/create'.format(api_url)
    paste_url = ''

    def get_encoded_paste(self, data):
        """
        Returns a urlencoded paste from the dictionary "data"
        """
        return parse.urlencode(data).encode()

    def send_paste(self, data):
        """
        Sends out a paste to the correct pastebin
        """
        request = req.Request(self.create_url, data=data)
        response = req.urlopen(request)
        return response.read().decode('utf-8')

    def get_langs(self):
        """
        Gets a dict of supported languages from the pastebin.
        """
        request = req.Request('{}/langs'.format(self.api_url))
        response = req.urlopen(request)
        return json.loads(response.read().decode('utf-8'))
