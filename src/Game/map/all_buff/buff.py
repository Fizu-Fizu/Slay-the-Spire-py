import math

class Buff:
    # 持续时间
    duration: int = 0
    # 触发
    # 每一回合开始
    on_turn_start: bool = False
    # 牌使用
    on_card_play: bool = False
    # 每一回合结束
    on_turn_end: bool = False
    # 被伤害
    on_damage_taken: bool = False
    # 被攻击
    on_attacked: bool = False
    on_attacked_effect: list = [0, 0] # 触发效果: [效果类型: 1、增减伤害数值;2、百分比增减, 触发效果参数]
    # 攻击时
    on_attack: bool = False
    on_attack_effect: list = [0, 0] # 触发效果: [效果类型：1、增减伤害数值;2、百分比增减, 触发效果参数]
    # 格挡时
    on_block: bool = False

    def __init__(self, duration: int, on_turn_start: bool, on_card_play: bool, on_turn_end: bool, on_damage_taken: bool, on_attacked: bool, on_attack: bool, on_block: bool):
        super().__init__(duration, on_turn_start, on_card_play, on_turn_end, on_damage_taken, on_attacked, on_attack, on_block)

# 攻击时触发
def trigger_attack(buffs: list[Buff], base_damage: int) -> int:
    damage = base_damage
    # 遍历增益/减益
    for on_attack_buff in buffs:
        effect_1 = [effect for effect in on_attack_buff.on_attack_effect if effect[0] == 1]
        effect_2 = [effect for effect in on_attack_buff.on_attack_effect if effect[0] == 2]
        for effect in effect_1:
            damage += effect[1]
        for effect in effect_2:
            damage *= 1 + effect[1]
            math.floor(damage)
    return damage

# 被攻击触发
def trigger_attacked(buffs: list[Buff], base_damage: int):
    damage = base_damage
    # 遍历增益/减益
    for on_attacked_buff in buffs:
        effect_1 = [effect for effect in on_attacked_buff.on_attacked_effect if effect[0] == 1]
        effect_2 = [effect for effect in on_attacked_buff.on_attacked_effect if effect[0] == 2]
        for effect in effect_1:
            damage += effect[1]
        for effect in effect_2:
            damage *= 1 + effect[1]
            math.floor(damage)
    return damage