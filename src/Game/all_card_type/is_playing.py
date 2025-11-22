from . import *
from ..start_game import Game, Object
from ..map import Player

# 使用卡牌
def use(self, hand_pile: list['Card'], discard_pile: list['Card'], exhaust_pile: list['Card']):
    if self.can_play and self in hand_pile:
        hand_pile.remove(self)
        self.trigger
        if self.delete:
            exhaust_pile.append(self)
            return True
        else:
            discard_pile.append(self)
            return True
    else:
        print("卡牌无法使用")
    return False

# 触发效果-模版
def trigger(self, player: 'Player', enemy: 'Object'):
    pass