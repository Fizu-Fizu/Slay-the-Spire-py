from ..all_card_type import Card
from ..start_game import Game
from ..common import trigger_attack, trigger_attacked
import random

# 使用卡牌
def use(self, hand_pile: list[Card], discard_pile: list[Card], exhaust_pile: list[Card]):
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
def trigger(self, player, enemy):
    from ..common import Player
    from ..object import Object
    # 类型: 1 攻击， 2 技能， 3  能力， 4 状态/诅咒
    # 触发攻击牌
    if self.type == 1:
        damage = self.use_attack()
        # 检索伤害增减buff
        buffs_on_attack = [buff for buff in Player.buff if buff.on_attack == True]
        # 触发效果
        damage = trigger_attack(buffs_on_attack, damage)
        # 删除变量
        del(buffs_on_attack)
        # 攻击
        if self.is_aoe:
            for enemy_ in enemy:
                buffs_on_attack = [buff for buff in enemy_.buff if buff.on_attacked == True]
                temp_damage = trigger_attacked(buffs_on_attack, damage)

from ..common import Room
# 洗牌
def shuffle(room: Room):
    if Room.player.draw_pile == []:
        Room.player.draw_pile = Room.player.discard_pile
        Room.player.discard_pile = []

# 抽牌
def draw(room: Room, num: int):
    while num > 0:
        if len(room.player.draw_pile) > 0:
            room.player.hand_pile.append(random.choice(room.player.draw_pile))
            room.player.draw_pile.remove(room.player.hand_pile[-1])
            num -= 1
        elif room.player.discard_pile != []:
            shuffle(room)
        else:
            return False
    return True
