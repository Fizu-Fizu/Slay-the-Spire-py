from .card import Card
from ..map import Buff

# 攻击牌
class Attack(Card):
    # 是否是AOE攻击
    is_aoe: bool
    # 伤害
    damage: int
    # 触发次数
    trigger_count: int
    # 增益/减益
    buff: list[list[bool, Buff]] = []

    # 构造函数
    def __init__(self, spend_energy: int, type: int, delete: bool, is_aoe: bool, damage: int):
        super().__init__(spend_energy, type, delete)
        self.is_aoe = is_aoe
        self.damage = damage
        self.trigger_count = 0


    # 攻击牌使用,输出基础伤害
    def use_attack(self) -> int:
        base_damage = self.damage
        return base_damage