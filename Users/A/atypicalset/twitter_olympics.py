## 2012 London Olympics

import scraperwiki
import simplejson
import urllib2
import datetime

# Change QUERY to your search term of choice.

QUERY_LIST = ['olympics', 'london2012']
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10000

for QUERY in QUERY_LIST:
    now = datetime.datetime.now()
    print str(now)
    for page in range(1, NUM_PAGES+1):
        base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
             % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
        try:
            results_json = simplejson.loads(scraperwiki.scrape(base_url))
            for result in results_json['results']:
                data = {}
                data['id'] = result['id']
                data['text'] = result['text']
                data['from_user'] = result['from_user']
                data['created_at'] = result['created_at']
                print data['from_user'], data['text'],data['from_user'],data['created_at']
                scraperwiki.sqlite.save(["id"], data)
        except:
            print 'Oh dear, failed to scrape %s' % base_url


## 2012 London Olympics

import scraperwiki
import simplejson
import urllib2
import datetime

# Change QUERY to your search term of choice.

QUERY_LIST = ['olympics', 'london2012']
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 10000

for QUERY in QUERY_LIST:
    now = datetime.datetime.now()
    print str(now)
    for page in range(1, NUM_PAGES+1):
        base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
             % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
        try:
            results_json = simplejson.loads(scraperwiki.scrape(base_url))
            for result in results_json['results']:
                data = {}
                data['id'] = result['id']
                data['text'] = result['text']
                data['from_user'] = result['from_user']
                data['created_at'] = result['created_at']
                print data['from_user'], data['text'],data['from_user'],data['created_at']
                scraperwiki.sqlite.save(["id"], data)
        except:
            print 'Oh dear, failed to scrape %s' % base_url


