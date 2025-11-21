class Game:
    """游戏类"""
    name: str
    max_HP: int
    HP: int
    gold: int
    relic: list
    now_node: int

    def __init__(self, name: str, max_HP: int, HP: int, gold: int, relic: list[int] = []):
        self.name = name
        self.max_HP = max_HP
        self.HP = HP
        self.gold = gold
        self.relic = relic
    
