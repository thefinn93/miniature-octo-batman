#!/usr/bin/env python
from powerline.lib.threaded import ThreadedSegment, with_docstring
import requests

statusURL = "http://att.mifiliberate/cgi/sysser.cgi?id=system_service&as=1&api=status"

def network(pl):
    """Returns the name of the carrier"""
    status = requests.get(statusURL).json()
    return [{
        "contents": status['statusBarNetwork'],
        "highlight_group": ["mifi:network"]
    }]

def connectionType(pl):
    """Displays the technology used to connect, ie. EDGE, 3G, HSPA(+), LTE"""
    status = requests.get(statusURL).json()
    return [{
        "contents": status['statusBarTechnology'].split(" ")[0],
        "highlight_group": ["mifi:connectionType"]
    }]

def GPS(pl):
    """Displays the status of the GPS. ie. Off, Searching, GotFix"""
    status = requests.get(statusURL).json()
    return [{
        "contents": status['statusBarGpsStatus'].split(" ")[0],
        "highlight_group": ["mifi:GPS"]
    }]
