# 导入标准库模块
import sys
import os

# 导入自定义模块
from src.start_game import new_game
from src.game.map.map import Map

# 常量定义
CHARACTER = [{
    "name": "The Silent",
    "Max HP": 70,
    "gold": 99,
    "Relic": [2],
}]

def main():
    """主函数"""
    _ = input("请按回车键开始游戏...")
    print("选择角色：\n")
    for i in range(len(CHARACTER)):
        print(f"{i + 1}. {CHARACTER[i]['name']}")
    input_num = -1
    while True:
        try:
            input_num = int(input("")) - 1
            if input_num >= 0 and input_num < len(CHARACTER):
                break
            else:
                print("请输入正确的数字！")
        except ValueError:
            print("请输入数字！")
    game_end = False
    GAME = new_game(
        2,########################################更改###########################################
        CHARACTER[input_num]["name"],
        CHARACTER[input_num]["Max HP"],
        CHARACTER[input_num]["gold"],
        CHARACTER[input_num]["Relic"]
        )
    while not game_end:
        os.system("cls")
        if GAME.map.map_all == []:
            GAME.map.plane_add()
        else:
            GAME.map.print_map()
        try:
            inp = int(input(f"m:地图\n输入1~{len(GAME.map.map_all[0])}进入对应节点\n0.退出").strip())
        except ValueError:
            if inp == "m":
                os.system("cls")
                GAME.map.print_map()
            else:
                print("请输入正确的数字！")
                continue
        if inp >= 1 and inp <= len(GAME.map.map_all[0]):
            os.system("cls")
            GAME.map.select_node(inp - 1, GAME)
        elif inp == 0:
            os.system("cls")
            game_end = True
        else:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
