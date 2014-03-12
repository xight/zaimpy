#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import codecs 
import unittest
from datetime import datetime
from datetime import timedelta
from pprint import pprint

from zaimapi import Zaim

sys.stdin  = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

consumer_key = unicode(os.environ.get("ZAIM_CONSUMER_KEY", ""))
consumer_secret = unicode(os.environ.get("ZAIM_CONSUMER_SECRET", ""))
access_token_key = unicode(os.environ.get("ZAIM_ACCESS_TOKEN_KEY", ""))
access_token_secret = unicode(os.environ.get("ZAIM_ACCESS_TOKEN_SECRET", ""))
assert consumer_key, 'Please set "ZAIM_CONSUMER_KEY".'
assert consumer_secret, 'Please set "ZAIM_CONSUMER_SECRET".'
assert access_token_key, 'Please set "ZAIM_ACCESS_TOKEN_KEY".'
assert access_token_secret, 'Please set "ZAIM_ACCESS_TOKEN_SECRET".'

zaim = Zaim(consumer_key, consumer_secret, access_token_key, access_token_secret)

class ZaimClassTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_genres(self):
        self.assertTrue(zaim.get_genres(self))

    def test_get_genres_by_name(self):
        genre = zaim.get_genre_by_name(u"食料品")
        genre_org = {
            u'active': 1,
            u'category_id': 101,
            u'created': u'2000-01-01 00:00:00',
            u'id': 10101,
            u'modified': u'2000-01-01 00:00:00',
            u'name': u'\u98df\u6599\u54c1',
            u'parent_genre_id': 10101,
            u'sort': 1
        }
        self.assertEqual(genre,genre_org)

    def test_get_genres_by_name_not_exist(self):
        with self.assertRaises(ValueError) as e:
            zaim.get_genre_by_name(u"not exist")

    def test_get_genre_id_by_name(self):
        self.assertTrue(zaim.get_genre_id_by_name(u"食料品"))

    def test_get_categories(self):
        self.assertTrue(zaim.get_categories(self))

    def test_get_category_by_name(self):
        category = zaim.get_category_by_name(u"食費")
        category_org = {
            u'active': 1,
            u'budget': 30000,
            u'calc': u'variable',
            u'color': u'#3a9625',
            u'created': u'2000-01-01 00:00:00',
            u'id': 101,
            u'image': u'restaurant',
            u'mode': u'payment',
            u'modified': u'2000-01-01 00:00:00',
            u'name': u'\u98df\u8cbb',
            u'parent_category_id': 101,
            u'sort': 1
        }
        self.assertEqual(category,category_org)

    def test_get_category_by_name_not_exist(self):
        with self.assertRaises(ValueError) as e:
            zaim.get_category_by_name(u"not exist")

    def test_get_category_id_by_name(self):
        self.assertTrue(zaim.get_category_id_by_name(u"食費"))

    def test_get_user(self):
        self.assertTrue(zaim.get_user())

    def test_get_user_id(self):
        self.assertTrue(zaim.get_user_id())

    def test_get_accounts(self):
        self.assertTrue(zaim.get_accounts())

    def test_get_account_by_name(self):
        self.assertTrue(zaim.get_account_by_name(u"お財布"))

    def test_get_account_by_name_not_exist(self):
        with self.assertRaises(ValueError) as e:
            zaim.get_account_by_name(u"not exist")
    
    def test_get_currencies(self):
        self.assertTrue(zaim.get_currencies())

    def test_get_money_records(self):
        self.assertTrue(zaim.get_money_records())

    def test_get_money_record_by_id_not_exist(self):
        with self.assertRaises(ValueError) as e:
            zaim.get_money_record_by_id(u"0")

    def test_create_delete_pay(self):
        date = datetime.today() + timedelta(days=31)
        param = {
                'category_id': zaim.get_category_id_by_name(u"食費"),
                'genre_id': zaim.get_genre_id_by_name(u"食料品"),
                'amount': '200000',
                'date': date,
                'comment': 'API',
                'from_account_id': zaim.get_user_id(),
                }
        ret = zaim.create_pay(**param)
        self.assertTrue(ret["money"]["id"])

        self.assertTrue(zaim.get_money_record_by_id(ret["money"]["id"]))

        last_money_id = ret["money"]["id"]
        ret = zaim.delete_pay(last_money_id)
        self.assertTrue(ret["money"]["id"])

    def test_delete_pay_not_exist(self):
        with self.assertRaises(ValueError) as e:
            zaim.delete_pay(u"1")

if __name__ == '__main__':
    unittest.main()
