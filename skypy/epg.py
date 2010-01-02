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
        self.initData = None
    
    def _getInitData(self):
        """
        Method to get the initialisation data.
        """
        if not self.initData:
            self.initData = json.loads(_getURL(EPG_INIT_URL))
        return self.initData
    
    def channels(self, genreFilter=None, cnoFilter=None, cidFilter=None):
        """
        Method to get list of channels with some basic filtering.
        """
        channels = self._getInitData().get('channels', None)
        if not channels:
            return None
        if genreFilter and len(genreFilter) > 0:
            channels = filter(lambda c: c.get('epggenre') in genreFilter, channels)
        if cnoFilter and len(cnoFilter) > 0:
            channels = filter(lambda c: c.get('channelno') in cnoFilter, channels)
        if cidFilter and len(cidFilter) > 0:
            channels = filter(lambda c: c.get('channelid') in cidFilter, channels)
        return channels
    
    def genres(self):
        """
        Method to get list of genres supported by EPG
        """
        return self._getInitData().get('epggenre', None)
    
    def channelsByGenre(self, genreFilter=None):
        """
        Method to get channels grouped by genre
        """
        genreId = [g.get('genreid') for g in self.genres()]
        if genreFilter and len(genreFilter) > 0:
            genreId = [gid for gid in genreId if gid in genreFilter]
        
        channels = {} # Dict with key : genreId and value : channel obj
        for channel in self.channels(genreFilter=genreId):
            epggenre = channel.get('epggenre')
            if not channels.get(epggenre, None):
                channels[epggenre] = []
            channels[epggenre].append(channel)
        return channels
    
    def channelsByGenreName(self, genreName=None):
        """
        Method to get channels by genre name
        """
        if not genreName:
            return None
        genreId = None
        for genre in self.genres():
            if genre.get('name').lower().find(genreName.lower()) != -1:
                genreId = genre.get('genreid')
                break
        return self.channelsByGenre(genreFilter=[genreId])
    
    def movieChannels(self):
        """
        Convenient method to get all movie channels
        """
        return self.channelsByGenreName('movies')
    
    def musicChannels(self):
        """
        Convenient method to get all music channels
        """
        return self.channelsByGenreName('music')
    
    def newsChannels(self):
        """
        Convenient method to get all news channels
        """
        return self.channelsByGenreName('news')

def main():
    e = epg()
    #print e.channels()
    #print e.genres()
    #print e.channelsByGenre()
    print e.movieChannels()
    
if __name__ == "__main__":
    main()
