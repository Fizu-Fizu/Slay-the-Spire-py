import json

class Relic:
    """遗物类"""
    name: str
    # 触发时机:
    # # 战斗开始
    on_battle_start: bool = False
    # 规则：[触发效果, 触发次数]触发效果: 1: 摸牌，
    on_battle_start_effect: list[int] = []
    # 战斗结束
    on_battle_end: bool = False
    # 战斗中:
    # 每一回合开始
    on_turn_start: bool = False
    # 牌使用
    on_card_play: bool = False 
    # 每一回合结束
    on_turn_end: bool = False 
    # 牌攻击触发
    on_attack: bool = False 
    # 牌格挡触发
    on_block: bool = False 
    # 对方攻击
    # 被伤害触发
    on_damage_taken: bool = False 
    # 被攻击触发
    on_attacked: bool = False 
    # 死亡？# 死亡触发
    on_death: bool = False
    trigger_variables = [
    "on_battle_start",
    "on_battle_end",
    "on_turn_start",
    "on_card_play",
    "on_turn_end",
    "on_attack",
    "on_block",
    "on_damage_taken",
    "on_attacked",
    "on_death",
    "on_battle_start_effect"
]
    def __init__(self, number_: int):
        number = str(number_)
        file_path = f'al_relic.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            if number in data:
                relic_data = data[number]
                if "on" in relic_data:
                    on_data_key = relic_data["on"].keys()
                    self.name = relic_data['name']
                    # 遗物处理
                    for i in on_data_key:
                        if i in self.trigger_variables:
                            setattr(self, i, relic_data["on"][i])
            
        except Exception as e:
            print(f"读取文件时发生错误: {e}")

    def trigger(self) -> int:
        return 1