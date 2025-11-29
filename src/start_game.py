from  .game.map.map import Map
from .game.map.node import Node
from .game.common.buff import Buff
from .game.common.relic import Relic
from .game.cards.card import Card

class Game:
    """游戏类"""
    user_ID: int
    name: str
    # 生命值
    max_HP: int
    HP: int
    # 护甲
    block: int
    # 金币
    gold: int
    # 遗物
    relic: list[Relic]
    # 节点
    now_node: Node
    #  buff
    buff: list[Buff]
    # 卡牌
    card: list[Card]
    # 地图
    map: Map
    # 卡牌背包
    all_card: list[Card] = []
    # 能量最大值&当前能量
    max_energy: int = 3

    def __init__(self, user_ID: int, name: str, max_HP: int, gold: int, relic: list[int] = []):
        """创建游戏"""
        self.user_ID = user_ID
        self.name = name
        self.max_HP = max_HP
        self.HP = max_HP
        self.gold = gold
        self.relic = [Relic(i) for i in relic]
        self.map = Map()
        self.now_node = self.map.map_all[0][0]
        temp = []
        if user_ID == 1:
            pass
        elif user_ID == 2:
            temp = [2001, 2001, 2001, 2001, 2001, 2301, 2301, 2301, 2301, 2301]
        for i in temp:
            self.all_card.append(Card(i))
    
    def prt_Game(self):
        """输出信息"""
        msg = "玩家信息: \n"
        if self.block > 0:
            msg = f"\033[36m格挡:{self.block}\033[0m "
        msg += (
                f"\033[31mHP:{self.HP}/{self.max_HP}\033[0m " +
                f""
            )
        print(msg)

def new_game(user_ID: int, name: str, max_HP: int, gold: int = 0, relic: list[int] = []) -> Game:
    """创建游戏"""
    GAME = Game(user_ID, name, max_HP, gold, relic)
    return GAME