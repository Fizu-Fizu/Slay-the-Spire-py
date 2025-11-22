# 卡牌
class Card:
    # 消耗的能量，如果是X，此值为None
    spend_energy: int
    # 类型: 1 攻击， 2 技能， 3  能力， 4 状态/诅咒
    type: int
    # 是否消耗
    delete: bool = False
    # 是否可打出
    can_play: bool = True

    # 初始化
    def __init__(self, spend_energy: int, type: int, delete: bool):
        self.spend_energy = spend_energy
        self.type = type
        self.delete = delete
    
    # 弃牌
    def discard(self, hand_pile: list['Card'], discard_pile: list['Card']):
        if self in hand_pile:
            hand_pile.remove(self)
            discard_pile.append(self)
            return True
        else:
            print("卡牌无法弃牌")
        return False
    
    # 输出卡牌-模版
    def prt_card(self):
        pass


    # 输出牌组
    def prt_pile(self, pile: list['Card']):
        for card in pile:
            card.prt_card()