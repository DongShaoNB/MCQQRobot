import configparser
import re
import os
import requests
import json
import loadconfig

readsettings = open('.\\config\\settings.json', 'r+', encoding='utf-8')
readsettingstext = readsettings.read()
loadsettings = json.loads(readsettingstext)
BlackBE = loadsettings['BlackBE']
BlackBEenable = BlackBE['enable']
BlackBEapi = BlackBE['api']
EmailTipWhitelist = loadsettings['EmailTipWhitelist']
ETWenable = EmailTipWhitelist['enable']
ETWapi = EmailTipWhitelist['api']
ETWemail = EmailTipWhitelist['email']
# EWT stand for EmailTipWhitelist
BDS = loadsettings['BEBDS']
BDSServer = BDS['enable']
PlayerPostWhitelist = loadsettings['PlayerPostWhitelist']
PPWdisallow = PlayerPostWhitelist['disallow']
