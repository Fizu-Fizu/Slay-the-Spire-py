from ...all_card_type import *
from ...start_game import Game, Object

# 战斗
class TheBattle(Object):
    all_object: list[Object]
    # 战斗
    def __init__(self, enemy: list[Object]):
        for enemy_object in enemy:
            self.all_object.append(enemy_object)
    

    # 开始战斗
    def battleing(self, player: Game):
        while player.HP > 0:
            print("开始战斗,你的回合")

            while player.HP > 0 and self.all_object != []:
                1

# 玩家
class Player(Game):
    all_card: list[Card]
    hand_pile: list[Card]
    draw_pile: list[Card]
    discard_pile: list[Card]
    exhaust_pile: list[Card]