#!/usr/bin/python3

"""
py2deb - Release a debian package based on a python distutils setup file.

Copyright 2018 Ian Santopietro <isantop@gmail.com>
"""

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
