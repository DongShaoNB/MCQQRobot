#  Copyright (c) 2020 - 2021 DongShaoNB
#  该代码由DongShaoNB创建
#  由DongShaoNB一人编写
#  版权归DongShaoNB所有!

import os
from sendgroupmessage import *
from loadlanguage import *
from loadsettings import *


def autowhitelist(playerid, playerqq, group, allmessage):
    global qqh
    tfalready = os.path.isfile('whitelist//' + playerid + '.json')
    if not tfalready:
        files = os.listdir('whitelist//')
        for filename in files:
            # print('当前: %s' % filename)
            cf = open("whitelist//" + filename)
            jsonread = cf.read()
            jsonreadzz = json.loads(jsonread)
            qqh = str(jsonreadzz['qq'])
            cf.close()
            if qqh == str(playerqq):
                sendgroupmessage(group, SameQQReportWhitelist)
                break
        else:
            sendgroupmessage(group, WhitelistSuccessReportRobot)
            ReportWhitelistCommandInServer2 = ReportWhitelistCommandInServer.replace(
                '<playerid>', playerid)
            response = requests.post(seth + 'api/execute/',
                                     params={
                                         'apikey': setk
                                     },
                                     data={
                                         'name': sets,
                                         'command': ReportWhitelistCommandInServer2
                                     },
                                     headers={
                                         'User-Agent': 'MCQQRobot'
                                     })

            zj = json.loads(response.text)
            ztmm = zj['status']
            # 如果mcsm返回状态码200则发送信息提示成功并记录数据到白名单存储文本
            if ztmm == 200:
                sendgroupmessage(group, WhitelistSuccessReportServer)
                wj1 = allmessage['sender']
                wj2 = wj1['id']
                print('[MCQQRobot]新增白名单记录(' + str(wj2) + ":" + playerid + ')')
                wlj = open('whitelist//' + playerid + '.json', 'w')
                nr = {
                    "qq": playerqq,
                    "whitelist": "true"
                }
                wlj.write(json.dumps(nr))
                wlj.close()
                if ETWenable == "true":
                    response = requests.get(ETWapi,
                                            params={
                                                'email': ETWemail,
                                                'title': "白名单添加提示",
                                                'nr': "玩家" + playerid + "已成功添加白名单"
                                            },
                                            headers={
                                                'User-Agent': 'MCQQRobot'
                                            })
                    if response.text == "发送邮件成功！":
                        print("[MCQQRobot]邮件发送成功")
                    else:
                        print("[MCQQRobot]邮件发送失败，返回数据:" + response.text)
            else:
                WhitelistFailReportServer2 = WhitelistFailReportServer.replace('<status>',
                                                                               str(ztmm))
                sendgroupmessage(playerid, WhitelistFailReportServer2)

    elif tfalready:
        sendgroupmessage(group, SameGameIDReportWhitelist)
