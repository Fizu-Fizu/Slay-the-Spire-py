# 导入标准库模块
import sys
import os

# 导入自定义模块
from src import game

# 常量定义
THE_SILENT = {
    "name": "The Silent",
    "Max HP": 70,
    "HP": 70,
    "gold": 99,
    "Relic": [1],
}

def main():
    """主函数"""
    _ = input("请按回车键开始游戏...")
    game_end = False
    while not game_end:
        os.system("cls")
        print("hello world！")
    return 0


if __name__ == "__main__":
    sys.exit(main())
