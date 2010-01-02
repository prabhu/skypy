#!/usr/bin/env python
# encoding: utf-8
"""
API for accessing EPG data.

Author: Prabhu Subramanian
"""

from config import *
import json
import urllib2

def _getURL(url):
    """
    Method to invoke an url and return the data.
    """
    return urllib2.urlopen(url).read()

class epg(object):
    """
    Class supporting EPG related operations.
    """
    def __init__(self):
        pass
    
    def getInitData(self):
        """
        Method to get the initialisation data.
        """
        data = _getURL(EPG_INIT_URL)
        return data

def main():
    e = epg()
    print e.getInitData()

if __name__ == "__main__":
    main()
