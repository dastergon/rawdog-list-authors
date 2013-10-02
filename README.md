rawdog-list-authors
===================
Description
-----------
rawdog plugin to display authors list

Use `define_name`  under the feed entry.
Then add `__authors_list__` in template in order to display authors list.

e.g

    feed 30m http://example.com/feed.rss
        define_name John Smith

Installation
------------
To install a plugin, make sure that you have `plugindirs` plugins in your config file, and drop the plugin into your `~/.rawdog/plugins` directory.

Author
-----
Pavlos Ratis - (dastergon AT gentoo DOT org)
