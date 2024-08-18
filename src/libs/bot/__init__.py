import json
import websockets
import asyncio

class App:
    def __init__(self,uri,auth_key,name):
        self.auth_key = auth_key
        self.uri = uri
        self.headers = {"X-Auth-Key":self.auth_key}
        self.name = name

    async def _on_receive(self,websocket):
        while True:

            try:
                response = await websocket.recv()
                response = json.loads(response)

                print(f"\n{response['sender']}:{response['content']}")
                if response["content"] == "你是谁你是谁":
                    echo={"sender":self.name,
                          "type":"message",
                          "content":"我是中国的大美眉",
                          "time":"2024-8-5-17-17"}
                    await websocket.send(json.dumps(echo))

                if response["content"] == "ping":
                    echo={"sender":self.name,
                          "type":"message",
                          "content":"pong",
                          "time":"2024-8-5-17-17"}
                    await websocket.send(json.dumps(echo))

                echo={"sender":self.name,
                      "type":"message",
                      "content":response["content"],
                      "time":"2024-8-5-17-17"}
                await websocket.send(json.dumps(echo))


            except websockets.ConnectionClosed:
                print("Connection with server closed")
                break

    async def _start(self):
        async with websockets.connect(self.uri, extra_headers=self.headers) as websocket:
            # 启动接收消息的任务
            receive_task = asyncio.create_task(self._on_receive(websocket))

            # 等待任务完成
            await asyncio.gather(receive_task)

    def run(self):
        asyncio.run(self._start())