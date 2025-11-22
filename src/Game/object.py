from .common import Buff

class Object:
    """游戏对象类"""
    name: str
    # 生命值
    max_HP: int
    # 当前生命值
    HP: int
    # 格挡
    block: int
    # BUFF
    buff: list[Buff]