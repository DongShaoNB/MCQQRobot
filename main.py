from datetime import datetime
import tkinter.messagebox
from wlcheck import *
from removewhitelist import *
import websocket
from checkwhitelist import *
from adminremovewhitelist import *
from colorama import Fore, init
import time


# 时间
def nowtime():
    nowtime = time.strftime("%H:%M:%S", time.localtime())
    return nowtime


# 颜色自动恢复
init(autoreset=True)

# 检测版本是否为最新版
if tfcheckupdate == 'True' or tfcheckupdate == 'true':
    nra = requests.get("http://update.mcbeserver.cn:333/MCQQRobot/new.json")
    if nra.status_code != 200:
        print(Fore.RED + '[' + nowtime() + ' MCQQRobot]无法连接到更新服务器，HTTP状态码:' + str(nra.status_code))
    elif nra.status_code == 200:
        thenr = json.loads(nra.text.encode('utf-8'))
        nversion = thenr['version']
        tiptitle = thenr['title']
        text = thenr['text']
        if nversion != appversion:
            tkinter.Tk().withdraw()
            tkinter.messagebox.showinfo(title=tiptitle, message='有新版本：' + nversion + '\n' + text)
        elif nversion == appversion:
            print(Fore.GREEN + '[' + nowtime() + ' MCQQRobot]当前为最新版本!')

print(Fore.YELLOW + '[' + nowtime() + ' MCQQRobot]Mirai-Http-Api v2更改内容较多，建议前往MCQQRobot官方文档查看最新机器人配置方法')
print(Fore.YELLOW + '[' + nowtime() + ' MCQQRobot]http://docs.mcbeserver.cn/')

# 获取基础信息
# print('===============MCQQRobot==================\n'
#       '(1).启动服务        |        (2).检查更新\n'
#       '===============MCQQRobot==================')
# qs = input(Fore.BLUE + "请输入序号:")
# if qs == '2':
#     ht = input('请输入mirai-api-http中的host(例如:127.0.0.1)')
#     pt = input('请输入mirai-api-http中的port(例如:8080)')
#     ak = input('请输入mirai-api-http中的authKey')
#     aq = input('请输入机器人的QQ号')
#     sqg = input('请输入要启用的群号(技术有限，仅支持一个群，请谅解)')
#     qqowner = input('请输入机器人的主人，多个主人用|隔开')
#     mht = input('请输入mcsm的地址(例如:http://127.0.0.1:23333/)')
#     hk = input("请输入用户API KEY")
#     hsn = input("请输入服务器名字")
#
#     # 写入基础信息
#     htt = configparser.ConfigParser()
#     htt.read(".\\config\\config.ini")
#     htt.set("HP", "host", ht)
#     with open(".\\config\\config.ini", "w+") as h:
#         htt.write(h)
#
#     ptt = configparser.ConfigParser()
#     ptt.read(".\\config\\config.ini")
#     ptt.set("HP", "port", pt)
#     with open(".\\config\\config.ini", "w+") as y:
#         ptt.write(y)
#
#     aky = configparser.ConfigParser()
#     aky.read(".\\config\\config.ini")
#     aky.set("HP", "authkey", ak)
#     with open(".\\config\\config.ini", "w+") as s:
#         aky.write(s)
#
#     qa = configparser.ConfigParser()
#     qa.read(".\\config\\config.ini")
#     qa.set("HP", "qq", aq)
#     with open(".\\config\\config.ini", "w+") as s:
#         qa.write(s)
#
#     sqs = configparser.ConfigParser()
#     sqs.read(".\\config\\config.ini")
#     sqs.set("HP", "group", sqg)
#     with open(".\\config\\config.ini", "w+") as s:
#         sqs.write(s)
#
#     qow = configparser.ConfigParser()
#     qow.read(".\\config\\config.ini")
#     qow.set("HP", "owner", qqowner)
#     with open(".\\config\\config.ini", "w+") as q:
#         qow.write(q)
#
#     htt = configparser.ConfigParser()
#     htt.read(".\\config\\config.ini")
#     htt.set("MCSM", "http", mht)
#     with open(".\\config\\config.ini", "w+") as s:
#         htt.write(s)
#
#     hkk = configparser.ConfigParser()
#     hkk.read(".\\config\\config.ini")
#     hkk.set("MCSM", "key", hk)
#     with open(".\\config\\config.ini", "w+") as s:
#         hkk.write(s)
#
#     hn = configparser.ConfigParser()
#     hn.read(".\\config\\config.ini")
#     hn.set("MCSM", "server", hsn)
#     with open(".\\config\\config.ini", "w+") as s:
#         hn.write(s)
#
#     # 从httpapi获取sessionkey并绑定在机器人账号
#     url = 'http://' + sh + ':' + sp + "/auth"
#     data1 = {"authKey": sa}
#     r = requests.session()
#     s = r.post(url, json=data1)
#     bind = json.loads(s.text)
#     so = bind["session"]
#
#     gk = configparser.ConfigParser()
#     gk.read(".\\config\\config.ini")
#     gk.set("HP", "sessionkey", so)
#     with open(".\\config\\config.ini", "w+") as s:
#         gk.write(s)
#
#     url = 'http://' + sh + ':' + sp + "/verify"
#     data2 = {"sessionKey": so, "qq": sq}
#     r = requests.session()
#     s = r.post(url, json=data2)
#     fh2 = json.loads(s.text)
#     if fh2["msg"] == "success":
#         print(Fore.GREEN + '[MCQQRobot]机器人绑定成功')
#     else:
#         print(Fore.RED + '绑定过程中出现错误，请检查配置是否正常，有疑问请加入QQ群:159323818')
#
#
# elif qs == '4':
#     print('遇到问题请前往:http://help.mcbeserver.cn/index.php/mcqqrobot'
#           '如果网站内没有与您相同的问题的解决方案，请加QQ群159323818反馈，非常感谢！')

# if qs == '3':
#     vs = requests.get("http://update.mcbeserver.cn:333/MCQQRobot/version.html")
#     nra = requests.get("http://update.mcbeserver.cn:333/MCQQRobot/new.json")
#     thenr = json.loads(nra.text.encode('utf-8'))
#     nversion = thenr['version']
#     tiptitle = thenr['title']
#     text = thenr['text']
#     if nversion != appversion:
#         tkinter.Tk().withdraw()
#         tkinter.messagebox.showinfo(title=tiptitle, mes='有新版本：' + nversion + '\n' + text)
#     else:
#         tkinter.Tk().withdraw()
#         tkinter.messagebox.showinfo(title='当前软件版本为最新', mes='当前软件版本为最新')

if BlackBEenable == 'true':
    print(Fore.GREEN + '[' + nowtime() + ' MCQQRobot]云黑功能已启用')
else:
    print(Fore.RED + '[' + nowtime() + ' MCQQRobot]云黑功能已关闭')
if ETWenable == "true":
    print(Fore.GREEN + '[' + nowtime() + ' MCQQRobot]邮件通知功能已启用')
else:
    print(Fore.RED + '[' + nowtime() + ' MCQQRobot]邮件通知功能已关闭')
    # url = 'http://' + sh + ':' + sp + "/auth"
    # data1 = {"authKey": sa}
    # r = requests.session()
    # s = r.post(url, json=data1)
    # bind = json.loads(s.text)
    # so = bind["session"]
    #
    # gk = configparser.ConfigParser()
    # gk.read(".\\config\\config.ini")
    # gk.set("HP", "sessionkey", so)
    # gk.write(open(".\\config\\config.ini", "w+"))
    #
    # url2 = 'http://' + sh + ':' + sp + "/verify"
    # data2 = {"sessionKey": so, "qq": sq}
    # r = requests.session()
    # s = r.post(url2, json=data2)
    # fh2 = json.loads(s.text)
    # if fh2["msg"] == "success":
    #     print(Fore.GREEN + '[MCQQRobot]机器人绑定成功')
    #     url = 'ws://' + sh + ':' + sp + "/mes?sessionKey=" + sk
    #     print(Fore.GREEN + "[MCQQRobot]机器人对接成功，已启用！")
    #     gs = configparser.ConfigParser()
    #     gs.read(".\\config\\config.ini")
    #     sk = gs.get("HP", "sessionkey")
    # else:
    #     print(Fore.RED + '[MCQQRobot]绑定过程中出现错误，请检查配置是否正常，有疑问请加入QQ群:159323818')

    # 实时输出ws的内容


def on_message(ws, mes):
    mes = str(mes)
    mes = json.loads(mes)
    msdata = mes['data']
    print(Fore.BLUE + '[{time} MCQQRobot]{rec}'
          .format(time=nowtime(), rec=mes))
    mst = msdata['type']
    if mst == 'GroupMessage':
        si = msdata['sender']
        si2 = si["group"]
        si3 = si2["id"]
        if re.search(str(si3), sg):
            i1 = msdata['messageChain']
            sendq = msdata['sender']
            sendqq = str(sendq['id'])
            if BlackBEenable == 'true':
                response = requests.get(BlackBEapi + 'api/qqcheck?v2=true&qq=' + str(sendqq),
                                        headers={
                                            'User-Agent': 'MCQQRobot'
                                        })
                zj = json.loads(response.text)
                # print(response.text)
                ztm = zj['error']
                if ztm == 2002:
                    print(response.text)
                    datazj = zj['data']
                    playerid = datazj['name']
                    dangerlevel = datazj['level']
                    reason = datazj['info']
                    CheckBlackBEQQAndDanger2 = CheckBlackBEQQAndDanger.replace('<playerid>', playerid)
                    CheckBlackBEQQAndDanger3 = CheckBlackBEQQAndDanger2.replace('<playerqq>', sendqq)
                    CheckBlackBEQQAndDanger4 = CheckBlackBEQQAndDanger3.replace('<dangerlevel>', dangerlevel)
                    CheckBlackBEQQAndDanger5 = CheckBlackBEQQAndDanger4.replace('<reason>', reason)
                    sendgroupmessage(si3, CheckBlackBEQQAndDanger5)
                elif ztm == 2001:
                    sendgroupmessage(si3, CheckBlackBEQQAndPassing)
            if re.search("Plain", str(mes)):
                # 检测信息是否为文本
                if i1[1]["type"] == 'Plain':
                    i2 = i1[1]['text']
                    # 检测信息是否为申请白名单指令
                    if i2[0:7] == '.申请白名单 ':
                        rpnl = i2[7:].replace("\n", "")
                        autowhitelist(rpnl, sendqq, si3, mes)
                        #  ww = w1.read()
                        # w1 = open('whitelistb.txt', 'r')
                        # wj1 = mes['sender']
                        # wj2 = wj1['id']
                        # # 如果白名单存储文本中存在玩家申请的游戏名(即游戏名已经申请过了):
                        # if re.search(i2[6:], ww):
                        #     sendgroupmessage(si3, SameGameIDReportWhitelist)
                        #     # 如果白名单存储文本中存在申请人的QQ账号(即重复申请多个账号):
                        # elif re.search(str(wj2), ww):
                        #     sendgroupmessage(si3, SameQQReportWhitelist)
                        # else:
                        #     w1.close()
                        #     sendgroupmessage(si3, WhitelistSuccessReportRobot)
                        #     i2 = i1[1]['text']
                        #     PlayerReportName = i2[6:]
                        #     if re.search('\n', PlayerReportName.strip()):
                        #         zanshide = PlayerReportName.strip()
                        #         postwl = zanshide.replace('\n', '')
                        #     else:
                        #         postwl = PlayerReportName.strip()
                        #
                        #     ReportWhitelistCommandInServer2 = ReportWhitelistCommandInServer.replace(
                        #         '<playerid>', postwl)
                        #     response = requests.post(seth + 'api/execute/',
                        #                              params={
                        #                                  'apikey': setk
                        #                              },
                        #                              data={
                        #                                  'name': sets,
                        #                                  'command': ReportWhitelistCommandInServer2
                        #                              },
                        #                              headers={
                        #                                  'User-Agent': 'MCQQRobot'
                        #                              })
                        #
                        #     zj = json.loads(response.text)
                        #     ztmm = zj['status']
                        #     # 如果mcsm返回状态码200则发送信息提示成功并记录数据到白名单存储文本
                        #     if ztmm == 200:
                        #         sendgroupmessage(si3, WhitelistSuccessReportServer)
                        #         wj1 = mes['sender']
                        #         wj2 = wj1['id']
                        #         print('新增白名单记录(' + str(wj2) + ":" + postwl + ')')
                        #         wlj = open('whitelistb.txt', 'a')
                        #         wlj.write('\n' + str(wj2) + ':' + postwl)
                        #         wlj.close()
                        #     else:
                        #         WhitelistFailReportServer2 = WhitelistFailReportServer.replace('<status>',
                        #                                                                        str(ztmm))
                        #         sendgroupmessage(si3, WhitelistFailReportServer2)

                    elif i2[0:3] == '.开服':
                        sendq = msdata['sender']
                        sendqq = str(sendq['id'])
                        if re.search(sendqq, str(robotowner)):
                            response = requests.get(seth + 'api/start_server/' + sets,
                                                    params={
                                                        'apikey': setk
                                                    },
                                                    headers={
                                                        'User-Agent': 'MCQQRobot'
                                                    })
                            zj = json.loads(response.text)
                            ztm = zj['status']
                            if int(ztm) == 200:
                                StartServerSuccessSendToServer2 = StartServerSuccessSendToServer.replace(
                                    "<servername>", sets)
                                sendgroupmessage(si3, StartServerSuccessSendToServer2)
                            else:
                                errorinfo = zj['error']
                                StartServerSuccessSendToServerButStartFail2 = StartServerSuccessSendToServerButStartFail.replace(
                                    '<servername>', sets)
                                StartServerSuccessSendToServerButStartFail3 = StartServerSuccessSendToServerButStartFail2.replace(
                                    '<status>', str(ztm))
                                StartServerSuccessSendToServerButStartFail4 = StartServerSuccessSendToServerButStartFail3.replace(
                                    '<errorinfo>', errorinfo)
                                sendgroupmessage(si3, StartServerSuccessSendToServerButStartFail4)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:3] == '.关服':
                        sendq = msdata['sender']
                        sendqq = str(sendq['id'])
                        if re.search(sendqq, str(robotowner)):
                            response = requests.get(seth + 'api/stop_server/' + sets,
                                                    params={
                                                        'apikey': setk
                                                    },
                                                    headers={
                                                        'User-Agent': 'MCQQRobot'
                                                    })
                            zj = json.loads(response.text)
                            ztm = zj['status']
                            if int(ztm) == 200:
                                StopServerSuccessSendToServer2 = StopServerSuccessSendToServer.replace(
                                    "<servername>", sets)
                                sendgroupmessage(si3, StopServerSuccessSendToServer2)
                            else:
                                errorinfo = zj['error']
                                StopServerSuccessSendToServerButStopFail2 = StopServerSuccessSendToServerButStopFail.replace(
                                    '<servername>', sets)
                                StopServerSuccessSendToServerButStopFail3 = StopServerSuccessSendToServerButStopFail2.replace(
                                    '<status>', str(ztm))
                                StopServerSuccessSendToServerButStopFail4 = StopServerSuccessSendToServerButStopFail3.replace(
                                    '<errorinfo>', errorinfo)
                                sendgroupmessage(si3, StopServerSuccessSendToServerButStopFail4)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:5] == '.发送指令':
                        sendq = msdata['sender']
                        sendqq = str(sendq['id'])
                        if re.search(sendqq, str(robotowner)):
                            willsendtoserver = i2[5:]
                            response = requests.post(seth + 'api/execute/?apikey=' + setk,
                                                     data={
                                                         'name': sets,
                                                         'command': willsendtoserver
                                                     },
                                                     headers={
                                                         'User-Agent': 'MCQQRobot'
                                                     })
                            zj = json.loads(response.text)
                            ztm = int(zj['status'])
                            if ztm == 200:
                                SendCommandToServerSuccess2 = SendCommandToServerSuccess.replace(
                                    '<command>', willsendtoserver)
                                SendCommandToServerSuccess3 = SendCommandToServerSuccess2.replace(
                                    '<servername>', sets)
                                sendgroupmessage(si3, SendCommandToServerSuccess3)
                            else:
                                errorinfo = zj['error']
                                print(zj)
                                SendCommandToServerSuccessButServerReturnFail2 = SendCommandToServerSuccessButServerReturnFail.replace(
                                    '<command>', willsendtoserver)
                                SendCommandToServerSuccessButServerReturnFail3 = SendCommandToServerSuccessButServerReturnFail2.replace(
                                    '<servername>', sets)
                                SendCommandToServerSuccessButServerReturnFail4 = SendCommandToServerSuccessButServerReturnFail3.replace(
                                    '<status>', str(ztm))
                                SendCommandToServerSuccessButServerReturnFail5 = SendCommandToServerSuccessButServerReturnFail4.replace(
                                    '<errorinfo>', errorinfo)
                                sendgroupmessage(si3, SendCommandToServerSuccessButServerReturnFail5)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:3] == '.菜单':
                        sendgroupmessage(si3, Menu + '\nMCQQRobot ' + appversion + '\nMade by DongShaoNB')
                    elif i2[0:7] == '.查云黑QQ ':
                        if re.search("At", str(mes)):
                            atqq = str(i1[2]["target"])
                            response = requests.get(BlackBEapi + 'api/qqcheck',
                                                    params={
                                                        'v2': 'true',
                                                        'qq': atqq
                                                    },
                                                    headers={
                                                        'User-Agent': 'MCQQRobot'
                                                    })
                            zj = json.loads(response.text)
                            ztm = zj['error']
                            # print(zj)
                            # print(ztm)
                            if ztm == 2003:
                                CheckBlackBEQQ2 = CheckBlackBEQQ.replace('<playerqq>', atqq)
                                sendgroupmessage(si3, CheckBlackBEQQ2)
                            elif ztm == 2002:
                                datazj = zj['data']
                                playerid = datazj['name']
                                dangerlevel = datazj['level']
                                reason = datazj['info']
                                CheckBlackBEQQAndDanger2 = CheckBlackBEQQAndDanger.replace('<playerid>',
                                                                                           playerid)
                                CheckBlackBEQQAndDanger3 = CheckBlackBEQQAndDanger2.replace(
                                    '<playerqq>',
                                    atqq)
                                CheckBlackBEQQAndDanger4 = CheckBlackBEQQAndDanger3.replace(
                                    '<dangerlevel>',
                                    dangerlevel)
                                CheckBlackBEQQAndDanger5 = CheckBlackBEQQAndDanger4.replace('<reason>',
                                                                                            reason)
                                sendgroupmessage(si3, CheckBlackBEQQAndDanger5)
                            elif ztm == 2001:
                                CheckBlackBEQQAndPassing2 = CheckBlackBEQQAndPassing.replace(
                                    '<playerqq>', atqq)
                                sendgroupmessage(si3, CheckBlackBEQQAndPassing2)

                        else:
                            mbqq = str(i2[7:])
                            response = requests.get(BlackBEapi + 'api/qqcheck',
                                                    params={
                                                        'v2': 'true',
                                                        'qq': mbqq
                                                    },
                                                    headers={
                                                        'User-Agent': 'MCQQRobot'
                                                    })
                            zj = json.loads(response.text)
                            ztm = zj['error']
                            if ztm == 2003:
                                CheckBlackBEQQ2 = CheckBlackBEQQ.replace('<playerqq>', mbqq)
                                sendgroupmessage(si3, CheckBlackBEQQ2)
                            elif ztm == 2002:
                                datazj = zj['data']
                                playerid = datazj['name']
                                dangerlevel = str(datazj['level'])
                                reason = datazj['info']
                                CheckBlackBEQQAndDanger2 = CheckBlackBEQQAndDanger.replace('<playerid>',
                                                                                           playerid)
                                CheckBlackBEQQAndDanger3 = CheckBlackBEQQAndDanger2.replace(
                                    '<playerqq>',
                                    mbqq)
                                CheckBlackBEQQAndDanger4 = CheckBlackBEQQAndDanger3.replace(
                                    '<dangerlevel>',
                                    dangerlevel)
                                CheckBlackBEQQAndDanger5 = CheckBlackBEQQAndDanger4.replace('<reason>',
                                                                                            reason)
                                sendgroupmessage(si3, CheckBlackBEQQAndDanger5)
                            elif ztm == 2001:
                                CheckBlackBEQQAndPassing2 = CheckBlackBEQQAndPassing.replace(
                                    '<playerqq>', mbqq)
                                sendgroupmessage(si3, CheckBlackBEQQAndPassing2)
                    elif i2[0:7] == ".查云黑ID ":
                        if BlackBEenable == 'true':
                            pid = i2[7:]
                            response = requests.get(BlackBEapi + 'api/check',
                                                    params={
                                                        'v2': 'true',
                                                        'id': pid
                                                    },
                                                    headers={
                                                        'User-Agent': 'MCQQRobot'
                                                    })
                            zj = json.loads(response.text)
                            ztm = zj['error']
                            if ztm == 2003:
                                CheckBlackBEID2 = CheckBlackBEID.replace('<playerid>', pid)
                                sendgroupmessage(si3, CheckBlackBEID2)
                            elif ztm == 2002:
                                data = zj['data']
                                playerid = data['name']
                                dangerlevel = str(data['level'])
                                reason = data['info']
                                mbqq = str(data['qq'])
                                CheckBlackBEIDAndDanger2 = CheckBlackBEIDAndDanger.replace('<playerid>',
                                                                                           playerid)
                                CheckBlackBEIDAndDanger3 = CheckBlackBEIDAndDanger2.replace('<playerqq>',
                                                                                            mbqq)
                                CheckBlackBEIDAndDanger4 = CheckBlackBEIDAndDanger3.replace('<dangerlevel>',
                                                                                            dangerlevel)
                                CheckBlackBEIDAndDanger5 = CheckBlackBEIDAndDanger4.replace('<reason>',
                                                                                            reason)
                                sendgroupmessage(si3, CheckBlackBEIDAndDanger5)
                            elif ztm == 2001:
                                CheckBlackBEIDAndPassing2 = CheckBlackBEIDAndPassing.replace('<playerid>',
                                                                                             pid)
                                sendgroupmessage(si3, CheckBlackBEIDAndPassing2)
                        elif BlackBEenable == 'false':
                            sendgroupmessage(si3, WhenBlackBEdisableuseit)
                    elif i2[0:5] == ".查ID ":
                        if re.search(str(sendqq), str(robotowner)):
                            checkwhitelistqq(mes, i2[5:], si3)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:5] == ".查QQ ":
                        if re.search(str(sendqq), str(robotowner)):
                            checkwhitelistid(mes, i2[5:], si3)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:7] == ".删除白名单 ":
                        if re.search(str(sendqq), str(robotowner)):
                            adminremovewhitelist(i2[7:], si3)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:7] == ".添加白名单 ":
                        if re.search(str(sendqq), str(robotowner)):
                            adminaddwhtelist(i2[7:], si3)
                        else:
                            sendgroupmessage(si3, CantUse)
                    elif i2[0:5] == ".检查更新":
                        nra = requests.get("http://update.mcbeserver.cn:333/MCQQRobot/new.json")
                        thenr = json.loads(nra.text.encode('utf-8'))
                        nversion = thenr['version']
                        text = thenr['text']
                        if nversion != appversion:
                            sendgroupmessage(si3, "有新版本可以更新!\n版本号:" + nversion + "\n" + text)
                        else:
                            sendgroupmessage(si3, "当前已为最新版本")
                    # elif i2[0:5] == '.抽奖10':
                    #             wpid1 = str(random.randint(0, 452))
                    #             wpid2 = str(random.randint(0, 452))
                    #             wpid3 = str(random.randint(0, 452))
                    #             wpid4 = str(random.randint(0, 452))
                    #             wpid5 = str(random.randint(0, 452))
                    #             wpid6 = str(random.randint(0, 452))
                    #             wpid7 = str(random.randint(0, 452))
                    #             wpid8 = str(random.randint(0, 452))
                    #             wpid9 = str(random.randint(0, 452))
                    #             wpid10 = str(random.randint(0, 452))
                    #             sendgroupmessage(si3,
                    #                              '您的10连抽抽到的物品ID分别为:' + wpid1 + ',' + wpid2 + ',' + wpid3 + ',' + wpid4 + ',' + wpid5 + ',' + wpid6 + ',' + wpid7 + ',' + wpid8 + ',' + wpid9 + ',' + wpid10)
                    #
                    # elif i2[0:3] == '.抽奖':
                    #     wpid = random.randint(0, 452)
                    #     ChouJiang2 = ChouJiang.replace('<id>', str(wpid))
                    #     sendgroupmessage(si3, ChouJiang2)
                    # elif i2[0:5] == '.SF抽奖' or i2[0:5] == '.sf抽奖':
                    #     wpid = random.randint(0, 506)
                    #     sendgroupmessage(si3, "您在粘液科技中抽到的物品顺序为" + str(wpid))

    elif mst == 'MemberLeaveEventKick' or mst == 'MemberLeaveEventQuit':
        removewhitelist(mes)
        # si = mes['member']
        # si2 = si["group"]
        # si3 = si2["id"]
        # if re.search(str(si3), sg):
        #     if mst == 'MemberLeaveEventKick':
        #         waitdebl1 = mes['member']
        #         istqqgroup = waitdebl1['group']
        #         qqgroup = istqqgroup['id']
        #         istqq = waitdebl1['id']
        #         MemberKickedGroup2 = MemberKickedGroup.replace('<playerqq>', str(istqq))
        #         sendgroupmessage(qqgroup, MemberKickedGroup2)
        #         ff = open('whitelistb.txt')
        #         wlnr = ff.read()
        #         if re.search(str(istqq), wlnr):
        #             xx = wlnr.split('\n')
        #             # 删除头部两项
        #             xx.pop(0)
        #             xx.pop(0)
        #
        #             # 创建字典
        #             wlxx = {}
        #
        #             # 遍历获取键值加入字典
        #             for i in xx:
        #                 # 每项进行分割
        #                 key_value = i.split(":")
        #                 # 存入键值对
        #                 wlxx[key_value[0]] = key_value[1]
        #             # 通过键可访问值
        #             btname = wlxx[str(istqq)]
        #             WhitelistPlayerLeaveGroup2 = WhitelistPlayerLeaveGroup.replace('<playerid>', btname)
        #             sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroup2)
        #             response = requests.post(seth + 'api/execute/',
        #                                      params={
        #                                          'apikey': setk
        #                                      },
        #                                      data={
        #                                          'name': sets,
        #                                          'command': 'whitelist remove ' + btname
        #                                      },
        #                                      headers={
        #                                          'User-Agent': 'MCQQRobot'
        #                                      })
        #
        #             zj = json.loads(response.text)
        #             print('MCSM返回:' + response.text)
        #             ztm = zj["status"]
        #             # 如果mcsm返回提交成功则
        #             if ztm == 200:
        #                 WhitelistPlayerLeaveGroupRemoveSuccess2 = WhitelistPlayerLeaveGroupRemoveSuccess.replace(
        #                     '<playerid>', btname)
        #             sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveSuccess2)
        #             removeplayer = open('RemovedPlayers.txt', 'a')
        #             removeplayer.write('\n' + str(istqq) + ':' + btname)
        #             removeplayer.close()
        #     elif mst == 'MemberLeaveEventQuit':
        #         waitdebl1 = mes['member']
        #         istqqgroup = waitdebl1['group']
        #         qqgroup = istqqgroup['id']
        #         istqq = waitdebl1['id']
        #
        #         MemberQuitGroup2 = MemberQuitGroup.replace('<playerqq>', str(istqq))
        #         sendgroupmessage(qqgroup, MemberQuitGroup2)
        #         ff = open('whitelistb.txt')
        #         wlnr = ff.read()
        #         if re.search(str(istqq), wlnr):
        #             xx = wlnr.split('\n')
        #             # 删除头部两项
        #             xx.pop(0)
        #             xx.pop(0)
        #
        #             # 创建字典
        #             wlxx = {}
        #
        #             # 遍历获取键值加入字典
        #             for i in xx:
        #                 # 每项进行分割
        #                 key_value = i.split(":")
        #                 # 存入键值对
        #                 wlxx[key_value[0]] = key_value[1]
        #             # 通过键可访问值
        #             btname = wlxx[str(istqq)]
        #
        #             WhitelistPlayerLeaveGroup2 = WhitelistPlayerLeaveGroup.replace('<playerid>', btname)
        #             sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroup2)
        #             removeplayer = open('RemovedPlayers.txt', 'a')
        #             removeplayer.write('\n' + str(istqq) + ':' + btname)
        #             removeplayer.close()
        #
        #             response = requests.post(seth + 'api/execute/',
        #                                      params={
        #                                          'apikey': setk
        #                                      },
        #                                      data={
        #                                          'name': sets,
        #                                          'command': 'whitelist remove ' + btname
        #                                      },
        #                                      headers={
        #                                          'User-Agent': 'MCQQRobot'
        #                                      })
        #
        #             zj = json.loads(response.text)
        #             print('MCSM返回:' + response.text)
        #             ztm = zj["status"]
        #             # 如果mcsm返回提交成功则
        #             if ztm == 200:
        #                 WhitelistPlayerLeaveGroupRemoveSuccess2 = WhitelistPlayerLeaveGroupRemoveSuccess.replace(
        #                     '<playerid>', btname)
        #                 sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveSuccess2)
        #             else:
        #                 WhitelistPlayerLeaveGroupRemoveFail2 = WhitelistPlayerLeaveGroupRemoveFail.replace(
        #                     '<playerid>', btname)
        #                 WhitelistPlayerLeaveGroupRemoveFail3 = WhitelistPlayerLeaveGroupRemoveFail2.replace(
        #                     '<status>', str(ztm))
        #                 sendgroupmessage(qqgroup, WhitelistPlayerLeaveGroupRemoveFail3)


def on_error(ws, err):
    # print(Fore.RED + '[' + nowtime() + ' MCQQRobot]' + error)
    print(Fore.RED + '[{time} MCQQRobot]{error}'
          .format(time=nowtime(), error=err))


def on_close(ws):
    print(Fore.RED + '[' + nowtime() + ' MCQQRobot]与Mirai连接已关闭')


if __name__ == '__main__':
    ws = websocket.WebSocketApp("ws://localhost:8080/message",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                )
    ws.run_forever()
