from loadconfig import *
from pdjson import *
import requests
import time
from colorama import Fore, init

# 颜色自动恢复
init(autoreset=True)


def nowtime():
    nowtime = time.strftime("%H:%M:%S", time.localtime())
    return nowtime


def sendgroupmessage(group, message):
    url = "http://" + sh + ":" + sp + "/sendGroupMessage"

    data = {
        "target": group,
        "messageChain": [
            {"type": "Plain", "text": message}
        ]
    }

    postm = requests.session()
    receive = postm.post(url, json=data)
    rinfo = receive.text
    if is_json(rinfo):
        rinfo2 = json.loads(rinfo)
        zt = rinfo2['msg']
        print(Fore.GREEN + '[' + nowtime() + ' MCQQRobot]消息(' + message + ')已提交到机器人，返回:' + zt)
    else:
        print(Fore.RED + '[' + nowtime() + ' MCQQRobot]消息(' + message + ')无法提交到机器人，返回:' + rinfo)
