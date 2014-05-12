
# -*- coding: utf-8 -*-
"""
Author: Alex AUVOLAT <alex@adnab.me>
Homepage: http://adnab.me
Version: 1.0
License: MIT License
Thanks: SAEKI Yoshiyasu for original notifo_notify script

This plugin sends HTTP notifications to the server of your choice.
"""

import weechat
import urllib
import urllib2

## registration

weechat.register("http_notify", "Alex AUVOLAT", "1.0", "MIT License",
    "http_notify: Push notification to HTTP server of your choice", "", "")

## settings

script_options = {
    "http_url": "",
    "notify_pv": "on",
    "notify_all": "off",
}

for option, default_value in script_options.items():
    if weechat.config_get_plugin(option) == "":
        weechat.prnt("", weechat.prefix("error") + "http_notify: Please set option: %s" % option)
        weechat.prnt("", "http_notify: /set plugins.var.python.http_notify.%s %s" % (option, ("STRING" if default_value == "" else default_value)))

## functions

def postHttp(message, handler=None, nick=None, chan=None):
    # weechat.prnt("", "Send message: %s" % message)
    HTTP_URL = weechat.config_get_plugin("http_url")
    if HTTP_URL != "":
        url = HTTP_URL
        opt_dict = {
            "msg": message,
            "nick": nick,
            "chan": chan
            }
        opt = urllib.urlencode(opt_dict)
        req = urllib2.Request(url, opt)
        res = urllib2.urlopen(req)

def en(opt):
    return weechat.config_get_plugin(opt) == "on"

def signal_callback(data, signal, signal_data):
    d = weechat.info_get_hashtable("irc_message_parse", {"message": signal_data})

    chan = d["channel"] if d["channel"][0] == "#" else "PM"
    nick = d["nick"]
    msg = ":".join(d["arguments"].split(":")[1:])

    # weechat.prnt("", "Send message: chan %s, nick %s, %s" % (chan,nick,msg))

    if (chan == "PM" and en("notify_pv")) or en("notify_all"):
        postHttp(msg, nick=nick, chan=chan)
    return weechat.WEECHAT_RC_OK

weechat.hook_signal("*,irc_in_privmsg", "signal_callback", "")

