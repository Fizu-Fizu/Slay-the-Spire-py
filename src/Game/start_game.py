from .map import Map
from .map import Node
from .map import Buff
from .all_card_type import *

class Game:
    """游戏类"""
    name: str
    max_HP: int
    HP: int
    block: int
    gold: int
    relic: list
    now_node: Node
    buff: list[Buff]
    card: list[Card]
    map: Map

    def __init__(self, name: str, max_HP: int, HP: int, gold: int, relic: list[int] = []):
        """创建游戏"""
        self.name = name
        self.max_HP = max_HP
        self.HP = HP
        self.gold = gold
        self.relic = relic
        self.map = Map()
        self.now_node = self.map.map_all[0][0]
    
    def prt_Game(self):
        """输出信息"""
        msg = "HP:" + str(self.HP) + "/" + str(self.max_HP) + "  " + "护盾:" + str(self.block)


class Object:
    """游戏对象类"""
    name: str
    max_HP: int
    HP: int
    block: int
    buff: list[Buff]
    skill: list[list[int, list]]

def new_game(name: str, max_HP: int, HP: int, gold: int, relic: list[int] = []) -> Game:
    """创建游戏"""
    GAME = Game(name, max_HP, HP, gold, relic)
    return GAME