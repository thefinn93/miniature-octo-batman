#!/usr/bin/env python
from powerline.lib.threaded import ThreadedSegment, with_docstring
import requests

class BTCSegment(ThreadedSegment):
    interval = 300

    def set_state(self, exchange="bitstamp", currency="USD", **kwargs):
        self.exchange = exchange
        super(BTCSegment, self).set_state(**kwargs)

    def update(self, oldprice):
        price = None
        if self.exchange == "bitstamp":
            ticker = requests.get("https://www.bitstamp.net/api/ticker/").json()
            price = "$%s" % ticker['last']
        if price is not None:
            return price
        else:
            return "Unknown exchange \"%s\"" % exchange

    def render(self, price, **kwargs):
        return [{
            "contents": str(price),
            "hightlight_group": ["btc"]
            }]

btc = with_docstring(BTCSegment(),
"""Returns the current price of Bitcoin at the specified exchage
:param str exchange:
    The name of the exchange. Currently supported:

    * bitstamp (supported currencies: USD)

:param str currency:
    The currency being exchanged to. See above for available currencies for
    your exchange.
highlight groups: ``btc``
""")
