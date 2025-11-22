from ..all_card_type import draw, Card
from ..start_game import Game
from ..object import Object

# 开始战斗
def battleing(game: Game, enemy_: list[Object]):
    player = Player(game)
    enemy = enemy_
    Battle = Room(player, enemy)
    del(enemy)
    del(player)
    # 触发战斗开始效果
    battle_start_relics = [i for i in Battle.player.relic if i.on_battle_start]
    # 触发效果
    for relic in battle_start_relics:
        relic.trigger(Battle)
    # 战斗
    while Battle.player.HP > 0 and Battle.enemy.all_object != []:
        print("开始战斗,你的回合")
        draw(Battle.player.draw_pile, Battle.player.hand_pile, 5)
        # 触发回合开始遗物
        turn_start_relics = [i for i in Battle.player.relic if i.on_turn_start]
        for relic in turn_start_relics:
            relic.trigger(Battle)
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

class Room:
    """房间类"""
    player: Player
    # 玩家
    enemy: list[Object]
    # 敌人

    def __init__(self, player: Player, enemy: list[Object]):
        self.player = player
        self.enemy = enemy