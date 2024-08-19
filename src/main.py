from libs import bot
p_ad = "ws://106.53.104.224:2048"
my_app = bot.App(name="蔡徐坤",auth_key="caixukun66",uri=p_ad)




class Chess:
    def __init__(self,player:list):
        self.chessboard = [["#", "#", "#"] for i in range(0, 3)]
        self.mapping_table = {"左上": self.chessboard[0][0],
                              "中上":self.chessboard[0][1],
                              "右上":self.chessboard[0][2],
                              "左中":self.chessboard[1][0],
                              "中中":self.chessboard[1][1],
                              "右中":self.chessboard[1][2],
                              "左下":self.chessboard[2][1],
                              "中下":self.chessboard[2][1],
                              "右下":self.chessboard[2][2]
                              }
        self.player = (player,None)
        self.round = player[0]
        self.piece_map = {player[0]:"#",
                          player[1]:"@"}
    def place(self,player:str,choice):
        if self.mapping_table[choice] == "#" and self.player[1] != None and player in self.player:
            self.mapping_table[choice] = self.piece_map[player]
            return "落子成功"
        return "落子失败"

    def get_view(self):
        s=""
        for i in self.chessboard:
            for j in i:
                s+=j
            s+="\n"
        print(s)
        return s
class Manager:
    def __init__(self):
        self.sum = 0
        self.chessboard={}
        self.player_to_chessboard_map = {}

    def check_player(self,name) ->bool:
        """
        检查是否已经存在对局
        :param name:
        :return:
        """
        if name in self.player_to_chessboard_map:
            return True
        else:
            return False

    def creat_game(self,name):
        if not chess_manager.check_player(name):
            self.player_to_chessboard_map[name] = self.sum
            self.chessboard[self.sum] = Chess(name)
            self.sum+=1
            return "创建成功"
        return "创建失败"

    def join_game(self,name:str,id:str)->bool:
            try:
                id = int(id)
                if id not in self.player_to_chessboard_map:
                    return "棋局不存在"
                elif self.chessboard[id].player[1] is not None:
                    self.chessboard[id].player[1] = name


            except:
                return "错误的输入"

    def get_view(self,name):
        id = self.player_to_chessboard_map[name]

        try:
            return self.chessboard[id].get_view()
        except:
            return "未参与对局"

    def place(self,name,choice):
        id = self.player_to_chessboard_map(name)
        return self.chessboard[id].place(name,choice)

chess_manager=Manager()
@my_app.register("message")
async def sample(ws,send,sender,type,content,time):
    if content == "/new chess":
        r=chess_manager.creat_game(sender)
        await send(r)

@my_app.register("message")
async def sample(ws,send,sender,type,content:str,time):
    if content.split()[0] == "/join":
        r=chess_manager.join_game(sender,content.split()[1])
        await send(r)

@my_app.register("message")
async def sample(ws,send,sender,type,content:str,time):
    if content == "/view":
        r=chess_manager.get_view(sender)
        await send(r)

@my_app.register("message")
async def sample(ws,send,sender,type,content:str,time):
    if content.split()[0] == "/place":
        r=chess_manager.place(sender,content.split()[1])
        send(r)




note = """
               ______     __     __     ______     ______     ______     ______  
              /\  == \   /\ \  _ \ \   /\  ___\   /\  == \   /\  __ \   /\__  _\ 
              \ \  __<   \ \ \/ ".\ \  \ \ \____  \ \  __<   \ \ \/\ \  \/_/\ \/ 
               \ \_____\  \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
                \/_____/   \/_/   \/_/   \/_____/   \/_____/   \/_____/     \/_/ 
"""

if __name__ == "__main__":
    print(note)
    my_app.run()