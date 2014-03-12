#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re
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

    records = zaim.get_money_records()
    ret = []
    for d in records:
        if re.match("API", d["comment"], re.UNICODE):
            ret.append(d)

    for d in ret:
        print d["id"],
        print d["comment"]
        money_id = d["id"]
        zaim.delete_pay(money_id)

if __name__ == '__main__':
    main()
