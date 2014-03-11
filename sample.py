# coding: utf-8
import os
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
    print zaim.get_categories()
    print zaim.get_user_info()
    print zaim.get_currencies()
    print zaim.get_currency_sign("JPY")
    print zaim.get_money_records()
    print zaim.get_genre_by_name(u"食料品")
    print zaim.get_category_by_name(u"食費")

if __name__ == '__main__':
    main()
