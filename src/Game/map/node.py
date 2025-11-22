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
        # boss节点
        if self.type == 0:
            1
        # 商店节点
        elif self.type == 1:
            1
        # 休整节点
        elif self.type == 2:
            1
        # 小怪节点
        elif self.type == 3:
            1
        # 精英节点
        elif self.type == 4:
            1
        # 宝箱节点
        elif self.type == 5:
            1
        # 未知节点
        elif self.type == 6:
            1
        