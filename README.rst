Zaim API for Python
===================

Requirements
------------

- Python 2.7
- requests
- requests-oauthlib


Zaim API
--------

- Version 2.0.3


How to use
----------

Get access token
^^^^^^^^^^^^^^^^

::

    $ export ZAIM_CONSUMER_KEY="YOUR CONSUMER KEY"
    $ export ZAIM_CONSUMER_SECRET="YOUR CONSUMER SECRET"
    $ python get_access_token.py
    REQUEST_TOKEN: {u'oauth_token_secret': u'...', u'oauth_token': u'...', u'oauth_callback_confirmed': u'true'}
    AUTHORIZE_URL: https://auth.zaim.net/users/auth?oautu_token=...
    oauth_verifier? : 

Go to AUTHORIZE_URL and login to Zaim. Then copy oauth_verifier from browser source.

::

    <code>YOUR OAUTH VERIFIER IS HERE</code>

If you are developing an web service, oauth_verifier will be redirected to your service.

::

    # get_access_token.py
    zaim.get_request_token(callback_url=u"http://your-web-service/")


If you were able to successfully retrive oauth_verifier, you paste it into your Terminal.

::

    oauth_verifier? : YOUR_OAUTH_VERIFIER
    OAUTH_VERIFIER: YOUR_OAUTH_VERIFIER
    ACCESS_TOKEN: {u'oauth_token_secret': u'...', u'oauth_token': u'...'}


Test
^^^^

::

    $ export ZAIM_CONSUMER_KEY="YOUR CONSUMER KEY"
    $ export ZAIM_CONSUMER_SECRET="YOUR CONSUMER SECRET"
    $ export ZAIM_ACCESS_TOKEN_KEY="YOUR ACCESS TOKEN KEY"
    $ export ZAIM_ACCESS_TOKEN_SECRET="YOUR ACCESS TOKEN SECRET"
    $ python zaim_test.py

Import from file
^^^^^^^^^^^^^^^^

::

    $ cd tools
    $ python import.py < data.tsv


License
-------

The MIT License

ToDo
-------

* logging
* show records within specific range
* delete records within specific range
