import math

class Buff:
    # 持续回合
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
    # 键名
    trigger_variables = [
    "on_turn_start",
    "on_card_play",
    "on_turn_end",
    "on_damage_taken",
    "on_attacked",
    "on_attack",
    "on_block",
    "on_attacked_effect",
    "on_attack_effect"
]

    def __init__(self, number_: int):
        import json
        number = str(number_)
        file_path = f'src/Game/common/al_buff.json'
        try:
            # 读取JSON文件
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            # 检查键名
            if number in data:
                buff_data = data[number]
                if "on" in buff_data:
                    on_data_key = buff_data["on"].keys()
                    self.name = buff_data['name']
                    # buff处理
                    for i in on_data_key:
                        if i in self.trigger_variables:
                            setattr(self, i, buff_data["on"][i])
            
        except Exception as e:
            print(f"读取文件时发生错误: {e}")

## 攻击时触发
#def trigger_attack(buffs: list[Buff], base_damage: int) -> int:
#    damage = base_damage
#    # 分类攻击效果
#    attack_effect_type_1_buffs = [
#        buff for buff in buffs
#        if buff.on_attack_effect[0] == 1
#    ]
#    attack_effect_type_2_buffs = [
#        buff for buff in buffs
#        if buff.on_attack_effect[0] == 2
#    ]
#    # 触发效果
#    for buff_ in attack_effect_type_1_buffs:
#        if buff_.on_attack_effect[1] != None:
#            damage += buff_.on_attack_effect[1]
#        else:
#            damage += buff_.duration
#    for buff_ in attack_effect_type_2_buffs:
#        damage *= 1 + buff_.on_attack_effect[1]
#        math.floor(damage)
#    return damage

# 攻击触发
def trigger_damage(buffs: list[Buff], base_damage: int, effect_type: str) -> int:
    # 攻击效果
    damage = base_damage
    # 攻击效果分类类型
    effect_attr = "on_" + effect_type + "_effect"
    attar_type_1_buffs = [
        buff for buff in buffs
        if getattr(buff, effect_attr)[0] == 1
    ]
    attar_type_2_buffs = [
        buff for buff in buffs
        if getattr(buff, effect_attr)[0] == 2
    ]
    # 攻击效果
    for buff_ in attar_type_1_buffs:
        damage += getattr(buff_, effect_attr)[1]
    for buff_ in attar_type_2_buffs:
        damage *= 1 + getattr(buff_, effect_attr)[1]
        damage = math.floor(damage)
    # 触发效果
    return damage