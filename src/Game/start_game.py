from .map import Map
from .map import Node

class Game:
    """游戏类"""
    name: str
    max_HP: int
    HP: int
    gold: int
    relic: list
    now_node: Node
    map: Map

    def __init__(self, name: str, max_HP: int, HP: int, gold: int, relic: list[int] = []):
        self.name = name
        self.max_HP = max_HP
        self.HP = HP
        self.gold = gold
        self.relic = relic
        self.map = Map()
        self.now_node = self.map.map_all[0][0]

def new_game(name: str, max_HP: int, HP: int, gold: int, relic: list[int] = []) -> Game:
    """创建游戏"""
    GAME = Game(name, max_HP, HP, gold, relic)
    return GAME