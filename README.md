# miniature-octo-batman
(aka Finn's Collection of Powerline Segments)

This is my collection of powerline segments. They are broken into categories
(mostly by what program/protocol they track). Here is the complete list:

 * **cjdns**:
  *Note that these assume you have the `cjdnsadmin` library installed. If you
  don't, just cp `/path/to/cjdns/contrib/python/cjdnsadmin/cjdnsadmin.py` to
  your path*

  * *peers* shows the number of peers currently connected, separating
   auto-discovered local ETHInterface peers and other peers into separate
   parts.

   Highlight groups: `cjdns:peers`, `cjdns:localpeers`, both fallback to
   `system_load` if not specified.

## Installation

*This assumes you have [powerline](https://github.com/Lokaltog/powerline) installed*

First, get the actual code:

    pip install -U --user git+https://github.com/thefinn93/minature-octo-batman

then, add the segments to your theme. Edit
`~/.config/powerline/themes/<extension>/<theme>.json` and add the segments like
this (this only does the `cjdns.peers` segment, add more as needed):

```json
{
    "module": "miniatureOctoBatman.cjdns",
    "name": "peers"
}
```
Finally, define some colors (the defaults I picked are really pretty terrible,
feel free to suggest better ones). In
`~/.config/powerline/colorschemes/<extension>/<theme>.json`, define colors for
the various segments. Each segment has the colorgroups used listed, here is an
example for cjdns peers:

```json
"cjdns:peers": { "fg": "gray8", "bg": "gray1" },
"cjdns:localpeers": { "fg": "gray8", "bg": "gray2" }
```
