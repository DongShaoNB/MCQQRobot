#  Copyright (c) 2020 - 2021 DongShaoNB
#  该代码由DongShaoNB创建
#  由DongShaoNB一人编写
#  版权归DongShaoNB所有!
from sendgroupmessage import *
from loadlanguage import *
import os


def checkwhitelistqq(mes, playerid, group):
    tfalready = os.path.isfile('whitelist//' + playerid + '.json')
    if tfalready:
        cf = open("whitelist//" + playerid + ".json")
        gs = cf.read()
        qq1 = json.loads(gs)
        qq2 = str(qq1['qq'])
        CheckIDbindQQsuccess2 = CheckIDbindQQsuccess.replace("<playerid>", playerid)
        CheckIDbindQQsuccess3 = CheckIDbindQQsuccess2.replace("<playerqq>", qq2)
        sendgroupmessage(group, CheckIDbindQQsuccess3)
    else:
        CheckIDbindQQfail2 = CheckIDbindQQfail.replace("<playerid>", playerid)
        sendgroupmessage(group, CheckIDbindQQfail2)


def checkwhitelistid(mes, playerqq, group):
    files = os.listdir('whitelist//')
    for filename in files:
        # print('当前: %s' % filename)
        cf = open("whitelist//" + filename)
        jsonread = cf.read()
        jsonreadzz = json.loads(jsonread)
        qqh = str(jsonreadzz['qq'])
        cf.close()
        plid = filename.replace(".json", "")
        if qqh == str(playerqq):
            CheckQQbindIDsuccess2 = CheckQQbindIDsuccess.replace("<playerqq>", playerqq)
            CheckQQbindIDsuccess3 = CheckQQbindIDsuccess2.replace("<playerid>", plid)
            sendgroupmessage(group, CheckQQbindIDsuccess3)
            break
    else:
        CheckQQbindIDfail2 = CheckQQbindIDfail.replace("<playerqq>", playerqq)
        sendgroupmessage(group, CheckQQbindIDfail2)
