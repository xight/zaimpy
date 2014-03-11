# coding: utf-8
import os
import sys
import codecs
sys.stdin  = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

from zaimapi import Zaim
from pprint import pprint

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
    pprint(zaim.get_genres())
    pprint(zaim.get_accounts())
    pprint(zaim.get_categories())
    pprint(zaim.get_user())
    pprint(zaim.get_currencies())
    pprint(zaim.get_currency_sign("JPY"))
    pprint(zaim.get_money_records())
    pprint(zaim.get_genre_by_name(u"食料品"))
    pprint(zaim.get_category_by_name(u"食費"))

if __name__ == '__main__':
    main()
