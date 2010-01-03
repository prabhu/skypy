#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Unit tests for skypy api.

Author: Prabhu Subramanian
"""
from skypy.epg import epg
import unittest
from datetime import datetime

class tests(unittest.TestCase):
    
    def setUp(self):
        """
        Setup is used for creating a new instance of epg
        """
        self.epg = epg()
     
    def tearDown(self):
        """
        Make the object None for easy garbage collection.
        """
        self.epg = None
    
    def testRetrieveChannel(self):
        """ Test if we are able to retrieve channels """
        self.assert_(self.epg.channels())

    def testRetrieveGenre(self):
        """ Test if we are able to retrieve genre """
        self.assert_(self.epg.genres())

    def testRetrieveChannelsByGenre(self):
        """ Test if we are able to retrieve channels by genre """
        self.assert_(self.epg.channelsByGenre())

    def testRetrieveMovieChannels(self):
        """ Test if we are able to retrieve movie channels (by genre name) """
        self.assert_(self.epg.movieChannels())

    def testRetrieveChannelIds(self):
        """ Test if we are able to retrieve channel ids """
        self.assert_(self.epg.channelIds())

    def testRetrieveProgrammes(self):
        """ Test if we are able to retrieve programmes """
        channelIds = self.epg.channelIds()[1:3]
        self.assert_(channelIds)
        self.assert_(self.epg.programmes(channelFilter=channelIds))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
