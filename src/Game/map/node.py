import json
import random

class Node:
    # 节点类型,0-6 对应图标["💀","💰","🔥","👻","😈","💎","❓"]
    type: int
    # 距离boss的距离
    now_node: int
    # 节点图标
    icon: list[str] = ["💀", "💰", "🔥", "👻", "😈", "💎", "❓"]

    # 节点初始化
    def __init__(self, type: int, now_node: int):
        self.type = type
        self.now_node = now_node

    def get_icon(self) -> str:
        return self.icon[self.type]

def enter_node(self_: Node, plane: int, game):
    from ...start_game import Game
    from ..core.object import Object
    game: Game = game
    file_path = r'data\al_enemy_list.json'
    # boss节点
    if self_.type == 0:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            enemy_list = data[random.choice(data[str(12)])]#############增加位面更改这里-1   ！！位面*10+3！！
            enemy_ = []
            for i in enemy_list:
                enemy_.append(Object(i[0], i[1]))
            from .room.battle_time import battleing
            temp_tf = battleing(game, enemy_)
            if temp_tf:
                return True
            else:
                return False
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
    # 商店节点
    elif self_.type == 1:
        run_dialogue(-1, game)
    # 休整节点
    elif self_.type == 2:
        run_dialogue(-2, game)
    # 小怪节点
    elif self_.type == 3:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            enemy_list = data[random.choice(data[str(11)])]#############增加位面更改这里-1   ！！位面*10+1！！
            enemy_ = []
            for i in enemy_list:
                enemy_.append(Object(i[0], i[1]))
            from .room.battle_time import battleing
            temp_tf = battleing(game, enemy_)
            if temp_tf:
                return True
            else:
                return False
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
    # 精英节点
    elif self_.type == 4:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            enemy_list = data[random.choice(data[str(12)])]#############增加位面更改这里-1   ！！位面*10+2！！
            enemy_ = []
            for i in enemy_list:
                enemy_.append(Object(i[0], i[1]))
            from .room.battle_time import battleing
            temp_tf = battleing(game, enemy_)
            if temp_tf:
                return True
            else:
                return False
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
    # 宝箱节点
    elif self_.type == 5:
        run_dialogue(-3, game)
    # 未知节点
    elif self_.type == 6:
        if plane >= 0:
            run_dialogue(1, game)

def run_dialogue(number_: int, game):
    from ...start_game import Game
    game: Game = game
    from .room.dialogue import Dialogue
    now_dialogue = Dialogue(number_)
    now_dialogue.run(game)
