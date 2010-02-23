#!/usr/bin/env python
# encoding: utf-8
"""
API for issuing remote record requests.

Author: Prabhu Subramanian
"""

import sys
import os
import urllib2
from cookielib import CookieJar
from config import *
import json

def _doPOST(POST_DATA=LOGIN_POST_DATA, extra_headers=META_HEADERS, args=None, url=LOGIN_URL, cookies=None):
    """
    Method to login to sky
    """
    body = ''
    if POST_DATA:
        body = '&'.join([k+'='+v for k,v in POST_DATA.items()]) % args
    
    headers={
        'Accept-Encoding' : 'deflate',
        'Content-Length' : len(body),
    }
    if extra_headers:
        headers.update(extra_headers)
    
    request = urllib2.Request(url, body, headers)
    try:
        response = urllib2.urlopen(request)
        if not cookies:
            cookies = CookieJar()
            cookies.extract_cookies(response, request)
        cookie_handler= urllib2.HTTPCookieProcessor(cookies)
        redirect_handler= urllib2.HTTPRedirectHandler()
        opener = urllib2.build_opener(redirect_handler, cookie_handler)
        resp = opener.open(request)
        return cookies, resp.read()
    except urllib2.HTTPError, e:
        print >> sys.stderr, "Sky servers having some trouble - ", e
        raise e
    except urllib2.URLError, e:
        print >> sys.stderr, "Sky servers having some trouble - ", e
        raise e

def record(channel, event, cookies=None):
    """
    Method to remote record an event.
    
    @param channel: Channel ID
    @param event: Event ID
    @param cookies: Cookies after a successful login. None would force re-login.
    
    Return values -
    For success -
    {u'remoteRecordResult': {u'message': u'Success', u'code': u'0'}}
    
    Already started -
    {u'remoteRecordResult': {u'message': u'Error: Program has already started', u'code': u'2'}}
    
    Invalid event and channel combination -
    {u'remoteRecordResult': {u'message': u'Error: Program not found', u'code': u'1'}}
    """
    if not cookies:
        cookies, data = _doPOST(args={'username' : USERNAME, 'password' : PASSWORD})
    cookies, data = _doPOST(POST_DATA=None, cookies=cookies, url=REMOTE_RECORD_URL%dict(channel=channel, event=event))
    return cookies, json.loads(data)

def logout(cookies=None):
    """
    Method to logout from sky. This will avoid any accidental behaviour like upgrade etc by the implementing apps.
    """
    cookies, data = _doPOST(POST_DATA=None, cookies=cookies, url=LOGOUT_URL)
    return cookies
    
def main():
    cookies, resp = record(1002, 1464)
    print resp['remoteRecordResult']['message']
    logout(cookies)
    
if __name__ == '__main__':
	main()
