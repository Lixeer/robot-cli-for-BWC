from libs import bot
p_ad = "ws://106.53.104.224:2048"
my_app = bot.App(name="蔡徐坤",auth_key="caixukun66",uri=p_ad)

@my_app.register("message")
async def sample(ws,send,sender,type,content,time):
    if content == "hello":
        await send(f"hello {sender}")



if __name__ == "__main__":
    my_app.run()