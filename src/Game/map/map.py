from node import Node

class Map:
    # 地图
    map_all: list[list[Node]] = []
    # 地图长度
    map_length_: int = 0

    # 创建地图
    def map_create(self, map_length: int) -> list[list[Node]]:
        map_all = []
        return map_all

    # 创建地图类
    def __init__(self, map_length: int):
        self.map_length_ = map_length
        self.map_all = self.map_create(self.map_length_)
