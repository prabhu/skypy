EPG_INIT_URL = "http://www.sky.com/tvlistings-proxy/TVListingsProxy/init.json"
# datetime = 201001011910 (yyyymmdd hour min)
EPG_DET_URL = "http://www.sky.com/tvlistings-proxy/TVListingsProxy/tvlistings.json?detail=%(detail)d&dur=%(duration)d&time=%(time)s&channels=%(channels)s"

# Sky username and password here.
USERNAME = ''
PASSWORD = ''

META_HEADERS = {
    'Host' : 'www.sky.com',
    'Referer' : 'http://www.sky.com/epg/release/current/sky.htm',
    'X-Requested-With' : 'XMLHttpRequest',
    'Accept' : 'application/json, text/javascript, */*',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6',
}

# Before logging in, you should get the public key.
PUBLIC_KEY_URL = "http://www.sky.com/tvlistings-proxy/TVListingsProxy/getPublicKey.json?siteId=1"

# Thanks to single sign-on, we need not replicate the encryption logic to
# login.
# For interested people, the js which encrypts the password in tv listings
# page is http://www.sky.com/epg/release/current/js/epg_build.js. Look for
# method encryptedString.
LOGIN_URL = "https://skyid.sky.com/signin"

LOGIN_POST_DATA = {
    'username' : '%(username)s',
    'password' : '%(password)s',
}

# Url to send remote record requests.
REMOTE_RECORD_URL="http://www.sky.com/tvlistings-proxy/TVListingsProxy/remoteRecord.json?channelId=%(channel)d&eventId=%(event)d&siteId=1"
LOGOUT_URL = "http://www.sky.com/tvlistings-proxy/TVListingsProxy/logout.do"

# Load local configs containing username and password.
try:
    from local_config import *
except:
    pass
