#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import urlparse
import requests
from requests_oauthlib import OAuth1
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# Zaim API ver 2.0.3
API_ROOT = "https://api.zaim.net/v2/"

request_token_url = API_ROOT + "auth/request"
authorize_url = "https://auth.zaim.net/users/auth"
access_token_url = API_ROOT + "auth/access"


class Zaim(object):
    def __init__(self, consumer_key, consumer_secret, access_token_key=None, access_token_secret=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.set_access_token(access_token_key, access_token_secret)
        self.genres = {}
        self.categories = {}
        self.user_info = {}
        self.accounts = {}
        self.currencies = {}
        self.money_records = {}
        self.auth = OAuth1(self.consumer_key, self.consumer_secret, self.access_token_key, self.access_token_secret)

    def set_access_token(self, access_token_key, access_token_secret):
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

    def get_request_token(self, callback_url=u"http://example.com/"):
        auth = OAuth1(self.consumer_key, self.consumer_secret, callback_uri=callback_url)
        r = requests.post(request_token_url, auth=auth)
        r.raise_for_status()

        request_token = dict(urlparse.parse_qsl(r.text))
        return request_token

    def get_authorize_url(self, request_token):
        return "{0}?oauth_token={1}".format(authorize_url, request_token["oauth_token"])

    def get_access_token(self, request_token, oauth_verifier):
        auth = OAuth1(self.consumer_key, self.consumer_secret, request_token["oauth_token"], request_token["oauth_token_secret"], verifier=oauth_verifier)
        r = requests.post(access_token_url, auth=auth)
        r.raise_for_status()

        access_token = dict(urlparse.parse_qsl(r.text))
        return access_token

    def get_genres(self, mode=None):
        data = None
        if mode:
            data = {"mode": mode}

        if not self.genres:
            endpoint = API_ROOT + "home/genre"
            r = requests.get(endpoint, auth=self.auth)
            r.raise_for_status()
            self.genres = r.json()["genres"]

        return self.genres

    def get_categories(self, mode=None):
        data = None
        if mode:
            data = {"mode": mode}

        if not self.categories:
            endpoint = API_ROOT + "home/category"
            r = requests.get(endpoint, auth=self.auth)
            r.raise_for_status()
            self.categories = r.json()["categories"]

        return self.categories

    def get_user_info(self):
        if not self.user_info:
            endpoint = API_ROOT + "home/user/verify"
            r = requests.get(endpoint, auth=self.auth)
            r.raise_for_status()
            self.user_info = r.json()["me"]

        return self.user_info

    def get_currencies(self):
        if not self.currencies:
            endpoint = API_ROOT + "currency"
            r = requests.get(endpoint)
            r.raise_for_status()
            self.currencies = r.json()["currencies"]

        return self.currencies

    def get_currency_sign(self, currency_code):
        currencies = self.get_currencies()
        for d in currencies:
            if d["currency_code"] == currency_code:
                return d["unit"]

    def get_accounts(self):
        endpoint = API_ROOT + "home/account"

        if not self.accounts:
            r = requests.get(endpoint, auth=self.auth)
            r.raise_for_status()
            self.accounts =  r.json()["accounts"]

        return self.accounts

    def create_pay(self, **params):
        endpoint = API_ROOT + "home/money/payment"

        data = {
            "category_id": params["category_id"],
            "genre_id": params["genre_id"],
            "amount": unicode(params["amount"]),
            "date": params["date"].strftime("%Y-%m-%d"),
            "from_account_id": params["from_account_id"],
        }

        if params.has_key("name"):
            data["name"] = params["name"]

        if params.has_key("place"):
            data["place"] = params["place"]

        if params.has_key("comment"):
            data["comment"] = params["comment"]

        r = requests.post(endpoint, data=data, auth=self.auth)
        r.raise_for_status()

        return r.json()

    def delete_pay(self, money_id):
        endpoint = API_ROOT + "home/money/payment"

        data = {
            "id": money_id,
        }
        r = requests.delete(endpoint, data=data, auth=self.auth)
        r.raise_for_status()

        return r.json()

    def create_income(self, **params):
        endpoint = API_ROOT + "home/money/income"

        data = {
            "category_id": params["income_category"],
            "amount": unicode(params["amount"]),
            "date": params["date"].strftime("%Y-%m-%d") if params["date"] else "",
            "to_account_id": params["to_account_id"],
        }

        if params.has_key("comment"):
            data["comment"] = params["comment"]

        r = requests.post(endpoint, data=data, auth=self.auth)
        r.raise_for_status()

        return r.json()

    def get_money_records(self):
        if not self.money_records:
            endpoint = API_ROOT + "home/money"
            r = requests.get(endpoint, auth=self.auth)
            r.raise_for_status()
            self.money_records = r.json()["money"]

        return self.money_records

    def get_genre_by_name(self, name):
        genres = self.get_genres()
        for d in genres:
            if d["name"] == name:
                return d

    def get_category_by_name(self, name):
        categories = self.get_categories()
        for d in categories:
            if d["name"] == name:
                return d

    def get_genre_id_by_name(self, name):
        return self.get_genre_by_name(name)["id"]

    def get_category_id_by_name(self, name):
        return self.get_category_by_name(name)["id"]
