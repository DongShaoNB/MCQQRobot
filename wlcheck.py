#  Copyright (c) 2020 - 2021 DongShaoNB
#  该代码由DongShaoNB创建
#  由DongShaoNB一人编写
#  版权归DongShaoNB所有!


from sendgroupmessage import *
from loadlanguage import *
from loadsettings import *
from colorama import Fore, init

# 颜色自动恢复
init(autoreset=True)


def nowtime():
    nowtime = time.strftime("%H:%M:%S", time.localtime())
    return nowtime


def autowhitelist(playerid, playerqq, group, allmessage):
    if PPWdisallow == "false":
        global qqh, ReportWhitelistCommandInServer2
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
                if BDSServer == 'false':
                    ReportWhitelistCommandInServer2 = ReportWhitelistCommandInServer.replace(
                        '<playerid>', playerid)
                elif BDSServer == 'true':
                    ReportWhitelistCommandInServer2 = ReportWhitelistCommandInServer.replace(
                        '<playerid>', '"' + playerid + '"')
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
                if ztmm == 200:
                    sendgroupmessage(group, WhitelistSuccessReportServer)
                    wj1 = allmessage['sender']
                    wj2 = wj1['id']
                    print(Fore.GREEN + '[' + nowtime() + ' MCQQRobot]新增白名单记录(' + str(wj2) + ":" + playerid + ')')
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
                            print(Fore.GREEN + '[' + nowtime() + ' MCQQRobot]邮件发送成功')
                        else:
                            print(Fore.RED + '[' + nowtime() + ' MCQQRobot]邮件发送失败，返回数据:' + response.text)
                else:
                    WhitelistFailReportServer2 = WhitelistFailReportServer.replace('<status>',
                                                                                   str(ztmm))
                    sendgroupmessage(playerid, WhitelistFailReportServer2)

        elif tfalready:
            sendgroupmessage(group, SameGameIDReportWhitelist)

    elif PPWdisallow == 'true':
        sendgroupmessage(group, AdminDisallowWhitelist)


def adminaddwhtelist(playerid, group):
    sendgroupmessage(group, WhitelistSuccessReportRobot)
    global ReportWhitelistCommandInServer2
    if BDSServer == 'false':
        ReportWhitelistCommandInServer2 = ReportWhitelistCommandInServer.replace(
            '<playerid>', playerid)
    elif BDSServer == 'true':
        ReportWhitelistCommandInServer2 = ReportWhitelistCommandInServer.replace(
            '<playerid>', '"' + playerid + '"')
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
    if ztmm == 200:
        sendgroupmessage(group, WhitelistSuccessReportServer)
