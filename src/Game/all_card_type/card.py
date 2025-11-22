import random


class Card:
    spend_energy: int
    type: int
    delete: bool = False
    can_play: bool = True

    # 初始化
    def __init__(self, spend_energy: int, type: int, delete: bool):
        self.spend_energy = spend_energy
        self.type = type
        self.delete = delete

    # 抽牌
    def draw(self, all_card:list['Card'], hand_pile: list['Card'], num: int):
        for i in range(num):
            if len(all_card) > 0:
                hand_pile.append(random.choice(all_card))
                all_card.remove(hand_pile[-1])
            else:
                return num - i
        return 0
    
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