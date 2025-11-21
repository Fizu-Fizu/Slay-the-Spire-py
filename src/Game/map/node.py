class Node:
    # 节点类型,["💀","💰","🔥","👻","😈","💎","❓"]
    type: str
    # 节点编号
    now_node: int
    # 节点后继节点编号
    next_node: list[int]
    # 节点图标
    icon: list[str] = ["💀", "💰", "🔥", "👻", "😈", "💎", "❓"]

    # 节点初始化
    def __init__(self, type: str, now_node: int, next_node: list[int]):
        self.type = type
        self.now_node = now_node
        self.next_node = next_node
