import configparser
import re
import os
import requests
import json
import loadconfig

readsettings = open('.\\config\\settings.json', 'r+')
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
