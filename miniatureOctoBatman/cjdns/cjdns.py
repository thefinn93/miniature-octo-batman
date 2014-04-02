#!/usr/bin/env python
import cjdnsadmin

def peers(pl):
    """Returns the current number of peers connected"""
    try:
        cjdns = cjdnsadmin.connectWithAdminInfo()
    except:
        return None
    peercount = 0
    localpeers = 0
    page = 0
    more = True
    while more:
        table = cjdns.InterfaceController_peerStats(page)
        more = "more" in table
        page += 1
        for peer in table['peers']:
            if peer['state'] != "UNRESPONSIVE":
                if "user" in peer:
                    if peer['user'] == "Local Peers":
                        localpeers += 1
                    else:
                        peercount += 1
                else:
                    peercount += 1
    out = [
            {
                "contents": str(peercount),
                "highlight_group": ["cjdns:peers", "system_load"]
            }
        ]
    if localpeers > 0:
        out.append({
            "contents": str(localpeers),
            "highlight_group": ["cjdns:localpeers", "system_load"]
            })
    return out

if __name__ == "__main__":
    print peers(None)
