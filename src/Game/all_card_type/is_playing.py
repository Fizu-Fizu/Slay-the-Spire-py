from ..all_card_type import Card
from ..start_game import Game, Object
from ..map import Player, trigger_attack, trigger_attacked
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
def trigger(self, player: 'Player', enemy: 'Object'):
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

# 抽牌
def draw(all_card:list[Card], hand_pile: list[Card], num: int):
    for i in range(num):
        if len(all_card) > 0:
            hand_pile.append(random.choice(all_card))
            all_card.remove(hand_pile[-1])
        else:
            return num - i
    return 0
