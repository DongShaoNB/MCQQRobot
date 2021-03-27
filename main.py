# -*- coding: utf-8 -*-
import requests
import json
import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket
import aiowebsocket
import configparser
import re
import os
import tkinter.messagebox

# 检测白名单存储文本是否存在，不存在则从更新服务器获取
if not os.path.isfile('.\\whitelistb.txt'):
    tkinter.Tk().withdraw()
    tkinter.messagebox.showerror(title='错误', message='检测到缺少文件，软件自动下载缺少的文件')
    udd = 'http://update.mcbeserver.cn:333/MCWhitelist-Mirai/whitelistb.txt'
    ud = requests.get(udd)
    with open("whitelistb.txt", "wb") as udf:
        udf.write(ud.content)
else:
    pass

    # 检测版本是否为最新版
    cf = configparser.ConfigParser()
    cf.read(".\\config.ini")
    au = cf.get("Other", "autoupdate")

    vs = requests.get("http://update.mcbeserver.cn:333/MCWhitelist-Mirai/version.html")
    vc = configparser.ConfigParser()
    vc.read(".\\config.ini")
    nvs = vc.get("Other", "version")
    # 如果启动自动更新且版本不是最新自动调用更新程序
    if au == "True":
        if vs.text != nvs:
            os.system('update.exe')
        else:
            pass
    else:
        pass

print('请务必把mirai-api-http中的enableWebsocket设置为true，否则将无法连接上机器人')
# 获取基础信息
qs = input('跳过设置过程请输入1，否则请直接回车(第一次使用请勿跳过)')
if qs != '1':
    ht = input('请输入mirai-api-http中的host(例如:127.0.0.1)')
    pt = input('请输入mirai-api-http中的port(例如:8080)')
    ak = input('请输入mirai-api-http中的authKey')
    aq = input('请输入机器人的QQ号')
    sqg = input('请输入要启用的群号(技术有限，仅支持一个群，请谅解)')
    mht = input('请输入mcsm的地址(例如:http://127.0.0.1:23333/)')
    hk = input("请输入用户API KEY")
    hsn = input("请输入服务器名字")

    # 写入基础信息

    htt = configparser.ConfigParser()
    htt.read(".\\config.ini")
    htt.set("HP", "host", ht)
    with open(".\\config.ini", "w+") as h:
        htt.write(h)

    ptt = configparser.ConfigParser()
    ptt.read(".\\config.ini")
    ptt.set("HP", "port", pt)
    with open(".\\config.ini", "w+") as y:
        ptt.write(y)

    aky = configparser.ConfigParser()
    aky.read(".\\config.ini")
    aky.set("HP", "authkey", ak)
    with open(".\\config.ini", "w+") as s:
        aky.write(s)

    qa = configparser.ConfigParser()
    qa.read(".\\config.ini")
    qa.set("HP", "qq", aq)
    with open(".\\config.ini", "w+") as s:
        qa.write(s)

    sqs = configparser.ConfigParser()
    sqs.read(".\\config.ini")
    sqs.set("HP", "group", sqg)
    with open(".\\config.ini", "w+") as s:
        sqs.write(s)

    htt = configparser.ConfigParser()
    htt.read(".\\config.ini")
    htt.set("MCSM", "http", mht)
    with open(".\\config.ini", "w+") as s:
        htt.write(s)

    hkk = configparser.ConfigParser()
    hkk.read(".\\config.ini")
    hkk.set("MCSM", "key", hk)
    with open(".\\config.ini", "w+") as s:
        hkk.write(s)

    hn = configparser.ConfigParser()
    hn.read(".\\config.ini")
    hn.set("MCSM", "server", hsn)
    with open(".\\config.ini", "w+") as s:
        hn.write(s)

    # 获取基础信息

    gh = configparser.ConfigParser()
    gh.read(".\\config.ini")
    sh = gh.get("HP", "host")

    gp = configparser.ConfigParser()
    gp.read(".\\config.ini")
    sp = gp.get("HP", "port")

    gq = configparser.ConfigParser()
    gq.read(".\\config.ini")
    sq = gq.get("HP", "qq")

    ga = configparser.ConfigParser()
    ga.read(".\\config.ini")
    sa = ga.get("HP", "authkey")

    gs = configparser.ConfigParser()
    gs.read(".\\config.ini")
    ss = gs.get("HP", "sessionkey")

    # 从httpapi获取sessionkey并绑定在机器人账号

    url = 'http://' + sh + ':' + sp + "/auth"
    data1 = {"authKey": sa}
    r = requests.session()
    s = r.post(url, json=data1)
    bind = json.loads(s.text)
    so = bind["session"]

    gk = configparser.ConfigParser()
    gk.read(".\\config.ini")
    gk.set("HP", "sessionkey", so)
    with open(".\\config.ini", "w+") as s:
        gk.write(s)

    url = 'http://' + sh + ':' + sp + "/verify"
    data2 = {"sessionKey": so, "qq": sq}
    r = requests.session()
    s = r.post(url, json=data2)
    fh2 = json.loads(s.text)
    if fh2["msg"] == "success":
        print('机器人绑定成功')
    else:
        print('绑定过程中出现错误，请检查配置是否正常，有疑问请加入QQ群:')
else:
    gh = configparser.ConfigParser()
    gh.read(".\\config.ini")
    sh = gh.get("HP", "host")

    gp = configparser.ConfigParser()
    gp.read(".\\config.ini")
    sp = gp.get("HP", "port")

    ga = configparser.ConfigParser()
    ga.read(".\\config.ini")
    sa = ga.get("HP", "authkey")

    gs = configparser.ConfigParser()
    gs.read(".\\config.ini")
    sk = gs.get("HP", "sessionkey")

    url = 'ws://' + sh + ':' + sp + "/message?sessionKey=" + sk

    print("机器人对接成功，已经启用！")


    # 实时输出ws的内容
    async def startup(uri):
        async with AioWebSocket(uri) as aws:
            converse = aws.manipulator
            while True:
                mes = await converse.receive()
                mes = json.loads(mes)
                print('{time}-机器人返回数据: {rec}'
                      .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))

                mst = mes['type']
                if mst == 'GroupMessage':
                    si = mes['sender']
                    si2 = si["group"]
                    si3 = si2["id"]
                    gs = configparser.ConfigParser()
                    gs.read(".\\config.ini")
                    sg = gs.get("HP", "group")
                    if re.search(str(si3), sg):
                        i1 = mes['messageChain']
                        if re.search("Plain", str(mes)):
                            # 检测信息是否为文本
                            if i1[1]["type"] == 'Plain':
                                i2 = i1[1]['text']
                                # 检测信息是否为申请白名单指令
                                if i2[0:6] == '申请白名单 ':
                                    w1 = open('whitelistb.txt', 'r')
                                    ww = w1.read()
                                    wj1 = mes['sender']
                                    wj2 = wj1['id']
                                    # 如果白名单存储文本中存在玩家申请的游戏名(即游戏名已经申请过了):
                                    if re.search(i2[6:], ww):

                                        gh = configparser.ConfigParser()
                                        gh.read(".\\config.ini")
                                        sh = gh.get("HP", "host")

                                        gp = configparser.ConfigParser()
                                        gp.read(".\\config.ini")
                                        sp = gp.get("HP", "port")

                                        ga = configparser.ConfigParser()
                                        ga.read(".\\config.ini")
                                        sa = ga.get("HP", "authkey")

                                        gs = configparser.ConfigParser()
                                        gs.read(".\\config.ini")
                                        sk = gs.get("HP", "sessionkey")

                                        url = "http://" + sh + ":" + sp + "/sendGroupMessage"

                                        data = {
                                            "sessionKey": sk,
                                            "target": sg,
                                            "messageChain": [
                                                {"type": "Plain", "text": "该玩家名已提交过白名单，提交失败！"}
                                            ]
                                        }

                                        w = requests.session()
                                        wl = w.post(url, json=data)
                                        print(wl.text)
                                        # 如果白名单存储文本中存在申请人的QQ账号(即重复申请多个账号):
                                    elif re.search(str(wj2), ww):

                                        gh = configparser.ConfigParser()
                                        gh.read(".\\config.ini")
                                        sh = gh.get("HP", "host")

                                        gp = configparser.ConfigParser()
                                        gp.read(".\\config.ini")
                                        sp = gp.get("HP", "port")

                                        ga = configparser.ConfigParser()
                                        ga.read(".\\config.ini")
                                        sa = ga.get("HP", "authkey")

                                        gs = configparser.ConfigParser()
                                        gs.read(".\\config.ini")
                                        sk = gs.get("HP", "sessionkey")

                                        url = "http://" + sh + ":" + sp + "/sendGroupMessage"

                                        data = {
                                            "sessionKey": sk,
                                            "target": sg,
                                            "messageChain": [
                                                {"type": "Plain", "text": "该QQ账号已提交过白名单，提交失败！"}
                                            ]
                                        }

                                        w = requests.session()
                                        wl = w.post(url, json=data)
                                        print(wl.text)
                                        # 如果不存在(即未申请过)则提交到mcsm
                                    else:
                                        w1.close()
                                        gh = configparser.ConfigParser()
                                        gh.read(".\\config.ini")
                                        sh = gh.get("HP", "host")

                                        gp = configparser.ConfigParser()
                                        gp.read(".\\config.ini")
                                        sp = gp.get("HP", "port")

                                        gq = configparser.ConfigParser()
                                        gq.read(".\\config.ini")
                                        sq = gq.get("HP", "qq")

                                        ga = configparser.ConfigParser()
                                        ga.read(".\\config.ini")
                                        sa = ga.get("HP", "authkey")

                                        gs = configparser.ConfigParser()
                                        gs.read(".\\config.ini")
                                        sk = gs.get("HP", "sessionkey")

                                        gs = configparser.ConfigParser()
                                        gs.read(".\\config.ini")
                                        sg = gs.get("HP", "group")

                                        i2 = i1[1]['text']

                                        url = "http://" + sh + ":" + sp + "/sendGroupMessage"

                                        data = {
                                            "sessionKey": sk,
                                            "target": sg,
                                            "messageChain": [
                                                {"type": "Plain", "text": "白名单成功提交到机器人！"}
                                            ]
                                        }

                                        w = requests.session()
                                        wl = w.post(url, json=data)
                                        print(wl.text)

                                        sh = configparser.ConfigParser()
                                        sh.read(".\\config.ini")
                                        seth = sh.get("MCSM", "http")

                                        sk = configparser.ConfigParser()
                                        sk.read(".\\config.ini")
                                        setk = sk.get("MCSM", "key")

                                        srn = configparser.ConfigParser()
                                        srn.read(".\\config.ini")
                                        sets = sk.get("MCSM", "server")

                                        response = requests.post(seth + 'api/execute/',
                                                                 params={
                                                                     'apikey': setk
                                                                 },
                                                                 data={
                                                                     'name': sets,
                                                                     'command': 'whitelist add ' + i2[6:]
                                                                 },
                                                                 headers={
                                                                     'User-Agent': 'MCWhitelist',
                                                                 })

                                        zj = json.loads(response.text)
                                        ztm = zj["status"]
                                        # 如果mcsm返回提交成功则发送信息提示成功并记录数据到白名单存储文本
                                        if ztm == 200:
                                            gh = configparser.ConfigParser()
                                            gh.read(".\\config.ini")
                                            sh = gh.get("HP", "host")

                                            gp = configparser.ConfigParser()
                                            gp.read(".\\config.ini")
                                            sp = gp.get("HP", "port")

                                            gq = configparser.ConfigParser()
                                            gq.read(".\\config.ini")
                                            sq = gq.get("HP", "qq")

                                            ga = configparser.ConfigParser()
                                            ga.read(".\\config.ini")
                                            sa = ga.get("HP", "authkey")

                                            gs = configparser.ConfigParser()
                                            gs.read(".\\config.ini")
                                            sk = gs.get("HP", "sessionkey")

                                            gs = configparser.ConfigParser()
                                            gs.read(".\\config.ini")
                                            sg = gs.get("HP", "group")

                                            url = "http://" + sh + ":" + sp + "/sendGroupMessage"

                                            data3 = {
                                                "sessionKey": sk,
                                                "target": sg,
                                                "messageChain": [
                                                    {"type": "Plain", "text": "白名单成功提交到服务器！"}
                                                ]
                                            }

                                            w = requests.session()
                                            wl = w.post(url, json=data3)
                                            print(wl.text)
                                            wj1 = mes['sender']
                                            wj2 = wj1['id']
                                            print(str(wj2) + ":" + i2[6:])
                                            wlj = open('whitelistb.txt', 'a')
                                            wlj.write('\n' + str(wj2) + ':' + i2[6:])
                                            wlj.close()
                                        else:
                                            gh = configparser.ConfigParser()
                                            gh.read(".\\config.ini")
                                            sh = gh.get("HP", "host")

                                            gp = configparser.ConfigParser()
                                            gp.read(".\\config.ini")
                                            sp = gp.get("HP", "port")

                                            gq = configparser.ConfigParser()
                                            gq.read(".\\config.ini")
                                            sq = gq.get("HP", "qq")

                                            ga = configparser.ConfigParser()
                                            ga.read(".\\config.ini")
                                            sa = ga.get("HP", "authkey")

                                            gs = configparser.ConfigParser()
                                            gs.read(".\\config.ini")
                                            sk = gs.get("HP", "sessionkey")

                                            gs = configparser.ConfigParser()
                                            gs.read(".\\config.ini")
                                            sg = gs.get("HP", "group")
                                            url = "http://" + sh + ":" + sp + "/sendGroupMessage"

                                            data4 = {
                                                "sessionKey": sk,
                                                "target": sg,
                                                "messageChain": [
                                                    {"type": "Plain", "text": "白名单无法提交到服务器！错误码:" + str(ztm)}
                                                ]
                                            }

                                            w = requests.session()
                                            wl = w.post(url, json=data4)
                                            print(wl.text)


    if __name__ == '__main__':
        remote = 'ws://' + sh + ':' + sp + "/message?sessionKey=" + sk
        try:
            asyncio.get_event_loop().run_until_complete(startup(remote))
        except KeyboardInterrupt as exc:
            logging.info('Quit.')
