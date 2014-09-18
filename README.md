# miniature-octo-batman
(aka Finn's Collection of Powerline Segments)

This is my collection of powerline segments. They are broken into categories
(mostly by what program/protocol they track). Here is the complete list:

 * **cjdns**: stats relating to [cjdns](https://github.com/cjdelisle/cjdns).

  *Note that these assume you have the `cjdnsadmin` library installed. If you
  don't, just cp `/path/to/cjdns/contrib/python/cjdnsadmin/cjdnsadmin.py` to
  your path*

  * *peers* shows the number of peers currently connected, separating
   auto-discovered local ETHInterface peers and other peers into separate
   parts.

   Highlight groups: `cjdns:peers`, `cjdns:localpeers`.

  * *nodes* shows the total number of know nodes in the routing table.

   Highlight groups: `cjdns:nodes`

 * **web**: stats from random websites.

  *Note: Most of these require the python [requests](http://www.python-requests.org/) module.*

  * *btc* shows the current price of bitcoins on the exchange of your choice
  (currently only Bitstamp is supported).

   Highlight group: `btc`

 * **packages**: Mostly because if I called it *apt* it would break imports.
  Maybe I'll extend it to yum or whatever some day...

  * *AptUpgrades* shows the number of packages that can be upgraded. It takes
    a little longer to run than I'd like, and doesn't change all that often, so
    it's threaded and runs every 5 minutes.

    Highlight group: `packages:upgrades`

 * **mifi**: I added this while on a long ride with an AT&T MiFi Liberate. It
    pulls the current status off of the device via the http api. Note that the
    URL to pull this (mostly the hostname) may need to be changed, and is
    defined at the top. Eventually I'd like to look into a more proper
    preferences solution, but that's what I've got right now. So far only the
    following can be rendered:

  * *network*: displays the name of the carrier.

   Highlight group: `mifi:network`

  * *connectionType*: Displays the technology used to connect, such as LTE,
    HSPA, or EDGE.

   Highlight group: `mifi:connectionType`

  * *GPS*: Displays the status of the GPS, ie. Off, searching, gotfix.

   Highlight group: `mifi:GPS`

## Installation

*This assumes you have [powerline](https://github.com/Lokaltog/powerline) installed*

First, get the actual code:

    pip install -U --user git+https://github.com/thefinn93/miniature-octo-batman

then, add the segments to your theme. Edit
`~/.config/powerline/themes/<extension>/<theme>.json` and add the segments like
this (this only does the `cjdns.peers` segment, add more as needed):

```json
{
    "function": "miniatureOctoBatman.cjdns.peers"
}
```
Finally, define some colors. In
`~/.config/powerline/colorschemes/<extension>/<theme>.json`, define colors for
the various segments. Each segment has the colorgroups used listed, here is an
example for cjdns peers:

```json
{
    "cjdns:peers": { "fg": "gray8", "bg": "gray1" },
    "cjdns:localpeers": { "fg": "gray8", "bg": "gray2" }
}
```
