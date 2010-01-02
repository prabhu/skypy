#!/usr/bin/env python
# encoding: utf-8
"""
API for accessing EPG data.

Author: Prabhu Subramanian
"""

from config import *
import json
import urllib2
from datetime import datetime as dt

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
        
        @param genreFilter: List of genres to be used for filtering
        @param cnoFilter: List of channels numbers for filtering.
        @param cidFilter: List of channel ids for filtering
        
        @return List of channels
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
    
    def channelIds(self):
        """
        Method to return all channel ids
        """
        return [channel.get('channelid') for channel in self.channels()]
        
    def channelsByGenre(self, genreFilter=None):
        """
        Method to get channels grouped by genre
        
        @param genreFilter: List of genre id for filtering.
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

        @param genreName: Genre name
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
    
    def programmes(self, channelFilter=None, duration=24 * 60, time=dt.now().strftime('%Y%m%d%H%M'), detail=2):
        """
        Method to retrieve programme details for a channel.
        
        @param channelFilter: List of channel ids for filtering.
        @param duration: Duration in minutes
        @param time: Start time for the data. Default Current minute. Format - %Y%m%d%H%M
        @param detail: Level of details required. 2 retrieves short desc. 1 basic data. Not sure about all possible values.
        """
        if not channelFilter:
            channelFilter = self.channelIds()        
        data = _getURL(EPG_DET_URL%dict(duration=duration, detail=detail, time=time, channels=','.join(channelFilter)))
        return json.loads(data)
                
def main():
    e = epg()
    #print e.channels()
    #print e.genres()
    #print e.channelsByGenre()
    #print e.movieChannels()
    #print e.channelIds()
    print e.programmes(channelFilter=['2002',])
    
if __name__ == "__main__":
    main()
