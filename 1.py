import json
from ws4py.client.threadedclient import WebSocketClient
from loadconfig import *


class CG_Client(WebSocketClient):

    def opened(self):
        req = '{"event":"subscribe", "channel":"eth_usdt.deep"}'
        self.send(req)

    def closed(self, code, reason=None):
        print("[MCQQRobot]与Mirai-Http-Api断开连接，状态码:" + str(code))

    def received_message(self, resp):
        print(resp)


if __name__ == '__main__':
    ws = None
    try:
        ws = CG_Client('ws://127.0.0.1:8080/all?sessionKey=' + sk)
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
