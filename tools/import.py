#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zaimapi import Zaim
from pprint import pprint

sys.stdin  = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

consumer_key = unicode(os.environ.get("ZAIM_CONSUMER_KEY", ""))
consumer_secret = unicode(os.environ.get("ZAIM_CONSUMER_SECRET", ""))
access_token_key = unicode(os.environ.get("ZAIM_ACCESS_TOKEN_KEY", ""))
access_token_secret = unicode(os.environ.get("ZAIM_ACCESS_TOKEN_SECRET", ""))

def main():
    assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
    assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
    assert access_token_key, 'Please set "ZAIM_ACCESS_TOKEN_KEY".'
    assert access_token_secret, 'Please set "ZAIM_ACCESS_TOKEN_SECRET".'

    zaim = Zaim(consumer_key, consumer_secret, access_token_key, access_token_secret)

    for line in sys.stdin:
        itemList = line[:-1].split('\t')
        (date, genre_name, amount, account_name) = tuple(itemList)

        try:
            genre = zaim.get_genre_by_name(genre_name)
        except ValueError:
            genre = None

        try:
            account = zaim.get_account_by_name(account_name)
        except ValueError:
            account = None

        if genre and account:
            param = {
                'category_id': genre["category_id"],
                'genre_id'   : genre["id"],
                'amount'     : unicode(amount),
                'date'       : datetime.strptime(date,"%Y-%m-%d"),
                'comment'    : 'API',
                'from_account_id': account["id"],
            }

            ret = zaim.create_pay(**param)
            print "OK: " + line,
            print ret
        else:
            print "NG: " + line,

if __name__ == '__main__':
    main()
