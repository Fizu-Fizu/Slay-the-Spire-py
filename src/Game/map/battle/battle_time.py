from ...all_card_type import draw, Card
from ...start_game import Game, Object

# 战斗
class TheBattle(Object):
    all_object: list[Object]
    # 战斗
    def __init__(self, enemy: list[Object]):
        for enemy_object in enemy:
            self.all_object.append(enemy_object)
    

# 开始战斗
def battleing(game: Game, enemy_: list[Object]):
    player = Player(game)
    enemy = enemy_
    while player.HP > 0 and enemy.all_object != []:
        print("开始战斗,你的回合")
        draw(player.draw_pile, player.hand_pile, 5)
        # 触发遗物
        for relic_ in player.relic:
            1
# 玩家
class Player(Game):
    # 手牌
    hand_pile: list[Card]
    # 抽牌堆
    draw_pile: list[Card]
    # 弃牌堆
    discard_pile: list[Card]
    # 消耗牌堆
    exhaust_pile: list[Card]
    # 当前能量
    energy: int

    def __init__(self, game: Game):
        super().__init__(game.name, game.max_HP, game.HP, game.gold, game.relic)
        self.draw_pile = game.all_card
        self.energy = game.max_energy