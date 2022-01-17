#  Copyright (c) 2020 - 2021 DongShaoNB
#  该代码由DongShaoNB创建
#  由DongShaoNB一人编写
#  版权归DongShaoNB所有!

import os
from sendgroupmessage import *
from loadlanguage import *
from loadsettings import *


def adminremovewhitelist(playerid, qqgroup):
    global RemoveWhitelistCommandInServer2
    tfalready = os.path.isfile('whitelist//' + playerid + '.json')
    if not tfalready:
        AdminRemoveWhitelistButNotSave2 = AdminRemoveWhitelistButNotSave.replace("<playerid>", playerid)
        sendgroupmessage(qqgroup, AdminRemoveWhitelistButNotSave2)
    else:
        os.remove('whitelist//' + playerid + '.json')
        if BDSServer == "true":
            RemoveWhitelistCommandInServer2 = RemoveWhitelistCommandInServer.replace("<playerid>", '"' + playerid + '"')
        elif BDSServer == 'false':
            RemoveWhitelistCommandInServer2 = RemoveWhitelistCommandInServer.replace("<playerid>", playerid)
        response = requests.post(seth + 'api/execute/',
                                 params={
                                     'apikey': setk
                                 },
                                 data={
                                     'name': sets,
                                     'command': RemoveWhitelistCommandInServer2
                                 },
                                 headers={
                                     'User-Agent': 'MCQQRobot'
                                 })

        zj = json.loads(response.text)
        ztmm = zj['status']
        if ztmm == 200:
            AdminRemoveWhitelistSUccess2 = AdminRemoveWhitelistSUccess.replace("<playerid>", playerid)
            sendgroupmessage(qqgroup, AdminRemoveWhitelistSUccess2)
        else:
            AdminRemoveWhitelistButServerError2 = AdminRemoveWhitelistButServerError.replace("<playerid>", playerid)
            sendgroupmessage(qqgroup, AdminRemoveWhitelistButServerError2)
