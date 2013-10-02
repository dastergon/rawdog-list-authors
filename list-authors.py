"""
@description: rawdog plugin to display authors list
@author: Pavlos Ratis <dastergon@gentoo.org>
@version: 1.0

Use 'define_name'  under the feed entry.
Then add __authors_list__ in template in order to display authors list.

e.g
feed 30m http://example.com/feed.rss
        define_name John Smith
"""
import rawdoglib.plugins
from urlparse import urlparse


def output_bits(rawdog, config, bits):
    authors = {}
    for feed_url, feed in rawdog.feeds.items():
        if "define_name" in feed.args:
            author = feed.args["define_name"]
            #split feed url and keep the basic url
            url = urlparse(feed_url)
            authors[author] = url.scheme + '://' + url.netloc

    authors_list = ""
    for author, url in authors.items():
        authors_list += '<li><a href="' + url + '">' + author + '</a></li>\n'

    #declare __authors_list__ template variable and add all authors
    bits["authors_list"] = '<ul>\n' + authors_list + '</ul>\n'

    return True

rawdoglib.plugins.attach_hook("output_bits", output_bits)
