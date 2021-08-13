#  Copyright (c) 2020 - 2021 DongShaoNB
#  该代码由DongShaoNB创建
#  由DongShaoNB一人编写
#  版权归DongShaoNB所有!
import os
import re

from loadsettings import *
from loadconfig import *
from loadlanguage import *
from sendgroupmessage import *
from loadconfig import *


def removewhitelist(allmessage):
    # ------------------------------
    global qqh, filename, WhitelistPlayerLeaveGroupRemoveSuccess2
    si = allmessage['member']
    mst = allmessage['type']
    si2 = si["group"]
    si3 = si2["id"]
    files = os.listdir('whitelist//')
    # ------------------------------
    waitdebl1 = allmessage['member']
    istqqgroup = waitdebl1['group']
    qqgroup = str(istqqgroup['id'])
    istqq = str(waitdebl1['id'])
    # tfalready = os.path.isfile('whitelist//' + playerid + '.json')
    # ------------------------------
    if mst == "MemberLeaveEventKick":
        if re.search(qqgroup, sg):
            MemberKickedGroup2 = MemberKickedGroup.replace('<playerqq>', str(istqq))
            sendgroupmessage(qqgroup, MemberKickedGroup2)
            for filename in files:
                cf = open("whitelist//" + filename)
                jsonread = cf.read()
                jsonreadzz = json.loads(jsonread)
                qqh = str(jsonreadzz['qq'])
                cf.close()
                print(qqh + " " + istqq)
                if qqh == istqq:
                    playid = os.path.basename(filename)
                    quitgid = playid.replace(".json", "")
                    WhitelistPlayerLeaveGroup2 = WhitelistPlayerLeaveGroup.replace('<playerid>', quitgid)
                    sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroup2)
                    response = requests.post(seth + 'api/execute/',
                                             params={
                                                 'apikey': setk
                                             },
                                             data={
                                                 'name': sets,
                                                 'command': 'whitelist remove ' + quitgid
                                             },
                                             headers={
                                                 'User-Agent': 'MCQQRobot'
                                             })

                    zj = json.loads(response.text)
                    print('MCSM返回:' + response.text)
                    ztm = zj["status"]
                    # 如果mcsm返回提交成功则
                    if ztm == 200:
                        WhitelistPlayerLeaveGroupRemoveSuccess2 = WhitelistPlayerLeaveGroupRemoveSuccess.replace(
                            '<playerid>', quitgid)
                        sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveSuccess2)
                        os.remove("whitelist//" + playid)
                    else:
                        WhitelistPlayerLeaveGroupRemoveFail2 = WhitelistPlayerLeaveGroupRemoveFail.replace(
                            '<playerid>', quitgid)
                        WhitelistPlayerLeaveGroupRemoveFail3 = WhitelistPlayerLeaveGroupRemoveFail2.replace(
                            '<status>', str(ztm))
                        sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveFail3)
    elif mst == "MemberLeaveEventQuit":
        if re.search(qqgroup, sg):
            MemberQuitGroup2 = MemberQuitGroup.replace('<playerqq>', str(istqq))
            sendgroupmessage(qqgroup, MemberQuitGroup2)
            for filename in files:
                cf = open("whitelist//" + filename)
                jsonread = cf.read()
                jsonreadzz = json.loads(jsonread)
                qqh = str(jsonreadzz['qq'])
                cf.close()
                if qqh == istqq:
                    playid = os.path.basename(filename)
                    quitgid = playid.replace(".json", "")
                    WhitelistPlayerLeaveGroup2 = WhitelistPlayerLeaveGroup.replace('<playerid>', quitgid)
                    sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroup2)
                    response = requests.post(seth + 'api/execute/',
                                             params={
                                                 'apikey': setk
                                             },
                                             data={
                                                 'name': sets,
                                                 'command': 'whitelist remove ' + quitgid
                                             },
                                             headers={
                                                 'User-Agent': 'MCQQRobot'
                                             })

                    zj = json.loads(response.text)
                    print('MCSM返回:' + response.text)
                    ztm = zj["status"]
                    # 如果mcsm返回提交成功则
                    if ztm == 200:
                        WhitelistPlayerLeaveGroupRemoveSuccess2 = WhitelistPlayerLeaveGroupRemoveSuccess.replace(
                            '<playerid>', quitgid)
                        sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveSuccess2)
                        os.remove("whitelist//" + playid)
                    else:
                        WhitelistPlayerLeaveGroupRemoveFail2 = WhitelistPlayerLeaveGroupRemoveFail.replace(
                            '<playerid>', quitgid)
                        WhitelistPlayerLeaveGroupRemoveFail3 = WhitelistPlayerLeaveGroupRemoveFail2.replace(
                            '<status>', str(ztm))
                        sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveFail3)
