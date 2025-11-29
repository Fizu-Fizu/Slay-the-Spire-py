import json
from ..common.buff import Buff
from .intent import Intent

class Object:
    """游戏对象类"""
    # 对象ID
    object_id: int = 0
    # 对象位置
    position: int = 0
    # 对象名称
    name: str = "无"
    # 生命值
    max_HP: int
    # 当前生命值
    HP: int
    # 格挡
    block: int = 0
    # BUFF
    buff: list[Buff] = []
    # 第一个意图索引
    # [0] == None:: 则多种随机
    ## [1]为一个数组，哪几种随机，[2]为一个数组，代表了随机权重
    # [0] == 0::
    ## [1]如果是1，则根据位置设置初始意图，一个字典{0: 1}0的索引代表默认，其他索引是对应站位意图
    start_index: list = [0]
    # 意图
    intents: dict[Intent] = []

    trigger_variables = [
        "max_HP",
        "buff",
        "start_index"
    ]

    def __init__(self, object_id: int, position: int):
        self.object_id = object_id
        self.name = data[str(object_id)]['name']
        self.position = position
        file_path = r'data\al_object.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            object_data: dict = data[object_id]
            keys = object_data.keys()
            for key_ in keys:
                if key_ in self.trigger_variables:
                    setattr(self, key_, object_data[key_])
            for intent_ in object_data['intents']:
                new_intent = Intent(object_id, intent_)
                self.intents[intent_] = new_intent
            
        except Exception as e:
            print(f"读取文件时发生错误: {e}")