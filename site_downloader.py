# this python script is used to download the site

import urllib2
import re
import logging
import itertools

def download(url, user_agent='wswp', num_retries = 2):
    print 'Downloading:', url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'download error:',e.reason
        html = None

        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries - 1)
        
    return html

def crawl_sitemap(url):
    #logging.info('something')
    # downloading the sitemap file
    sitemap = download(url)

    # extracting the sitemap links
    links = re.findall('<loc>(.*?)</loc>',sitemap)

    # downloading each link
    for link in links:
        html = download(link)
        

#crawl_sitemap('http://example.webscraping.com/sitemap.xml')

# using the itertools to download the links in the website

for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/-%d' % page
    html = download (url)
    if html is None:
        break
    else:
        #print html
        pass





