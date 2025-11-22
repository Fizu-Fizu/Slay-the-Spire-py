from .node_type import NodeType

class Node:
    # 节点类型,0-6 对应图标["💀","💰","🔥","👻","😈","💎","❓"]
    type: int
    # 距离boss的距离
    now_node: int
    # 节点图标
    icon: list[str] = ["💀", "💰", "🔥", "👻", "😈", "💎", "❓"]

    # 节点初始化
    def __init__(self, type: int, now_node: int):
        self.type = type
        self.now_node = now_node

    def get_icon(self) -> str:
        return self.icon[self.type]

    def enter_node(self):
        if self.type == 0:
            1