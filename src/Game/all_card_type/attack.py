from .card import Card
from ..map import Buff

class Attack(Card):
    # 是否是AOE攻击
    is_aoe: bool
    # 伤害
    damage: int
    # 触发次数
    trigger_count: int
    # 增益/减益
    buff: list[list[bool, Buff]] = []
    def __init__(self, spend_energy: int, type: int, delete: bool, is_aoe: bool, damage: int):
        super().__init__(spend_energy, type, delete)
        self.is_aoe = is_aoe
        self.damage = damage
        self.trigger_count = 0

    def use_attack(self) -> int:
        base_damage = self.damage
        return base_damage