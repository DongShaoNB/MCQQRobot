from loadconfig import *
from loadlanguage import *
from pdjson import *

def sendgroupmessage(group, message):
    url = "http://" + sh + ":" + sp + "/sendGroupMessage"

    data = {
        "sessionKey": sk,
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
        print('[MCQQRobot]消息(' + message + ')已提交到机器人，返回:' + zt)
    else:
        print('[MCQQRobot]消息(' + message + ')无法提交到机器人，返回:' + rinfo)
