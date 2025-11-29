import json
import os
import random
import math

class Dialogue:
    # 事件ID
    dialogue_id: int
    # 事件名称
    dialogue_name: str
    # 事件内容
    dialogue_list: list[dict] = []
    # "question": 说明, "options": 选项, "trigger":  触发效果[触发效果, 其他参数, 下一个对话索引(索引一定是-1)]
    # 触发效果: 1、增减最大生命值, 2、增减生命值, 3、获得遗物
    # 如果不同角色效果不同, [1] == None, 然后去索引[2]的字典

    # 事件类型 ： 1、Info信息展示,2、Choice事件选择,3、Confirm二次确认(高风险)||辅助类型4+
    dialogue_type: int = 0

    def __init__(self, dialogue_id: int):
        file_path = r'data\al_dialogue.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.dialogue_id = dialogue_id
                self.dialogue_name = data[str(dialogue_id)]['dialogue_name']
                self.dialogue_list = data[str(dialogue_id)]['dialogue_list']
                self.dialogue_type = data[str(dialogue_id)]['dialogue_type']
        except Exception as e:
            print(f"读取文件时发生错误: {e}")


    # 触发效果
    def trigger(self, list_ : list, game):
        from ....start_game import Game
        game: Game = game
        # 增减最大生命值
        if list_[0] == 1:
            add_max_HP = 0
            if list_[1] != None:
                add_max_HP = list_[2]
            elif list_[1] == None:
                add_max_HP = list_[2][game.name]
            game.max_HP += add_max_HP
            game.HP += add_max_HP
            game.HP = min(game.HP, game.max_HP)
            game.HP = max(game.HP, 1)
        # 增减生命值
        elif list_[0] == 2:
            add_HP = 0
            if list_[1] == None:
                add_HP = list_[2][game.name]
            elif list_[1] == 1:
                add_HP = list_[2]
            elif list_[1] == 2:
                add_HP = game.max_HP * list_[2]
                add_HP = math.floor(add_HP)
            game.HP += add_HP
            game.HP = min(game.HP, game.max_HP)
            game.HP = max(game.HP, 1)
        # 获得遗物
        elif list_[0] == 3:
            from ...common.relic import Relic
            game.relic.append(Relic(list_[1]))
        # 升级卡牌
        elif list_[0] == 4:
            from ...cards.card import Card
            if list_[1] == None:
                while True:
                    os.system("cls")
                    all_not_up_key: list[int] = []
                    i = 0
                    for card_ in game.all_card:
                        card_: Card
                        if card_.card_id < 10000:
                            print(card_.prt_card())
                            all_not_up_key.append(i)
                        i += 1
                    try:
                        inp = int(input("请选择要升级的卡牌(输入0退出): ").strip()) - 1
                        if inp >= 0 and inp < len(game.all_card):
                            game.all_card[all_not_up_key[inp]].upgrade()
                            break
                        elif inp == -1:
                            return 0
                        else:
                            continue
                    except ValueError:
                        continue
                return -1
                
        # 卖东西
        elif list_[0] == -1:
            card_file_path = r'data\al_card.json'
            with open(card_file_path, 'r', encoding='utf-8') as f:
                card_data: dict = json.load(f)
            card_keys_ = card_data.keys()
            # 获取所有卡牌
            attack_keys = [card_key for card_key in card_keys_ if card_key[0] == str(game.user_ID) and card_data[card_key]['type'] in [1]]
            skill_keys = [card_key for card_key in card_keys_ if card_key[0] == str(game.user_ID) and card_data[card_key]['type'] in [2]]
            power_keys = [card_key for card_key in card_keys_ if card_key[0] == str(game.user_ID) and card_data[card_key]['type'] in [3]]
            # 抽取卡牌
            all_shop_card_ = []
            all_shop_card_.append(random.choice(attack_keys))
            all_shop_card_.append(random.choice(attack_keys))
            all_shop_card_.append(random.choice(skill_keys))
            all_shop_card_.append(random.choice(skill_keys))
            all_shop_card_.append(random.choice(power_keys))
            from ...cards.card import Card
            all_shop_card: list[Card] = []
            sale = random.randint(0, 4)
            for i in all_shop_card_:
                card = Card(i)
                if card.rarity == 1:
                    card.rarity = random.randint(45, 55)
                elif card.rarity == 2:
                    card.rarity = random.randint(68, 82)
                elif card.rarity == 3:
                    card.rarity = random.randint(135, 165)
                all_shop_card.append(card)
            
            all_shop_card[sale].description += "打折出售！！"
            all_shop_card[sale].rarity /= 2
            math.floor(all_shop_card[sale].rarity)
            
            #############无色牌暂时未做!!!!!!!!! += 2
            while True:
                try:
                    os.system("cls")
                    ii = 1
                    for i in all_shop_card:
                        print(f"{ii}: ")
                        if i.name != "卖完了":
                            print(i.prt_card())
                            print(f"价格: {i.rarity}")
                        else:
                            print("卖完了")
                            print("")
                        ii += 1
                    inp = int(input("请选择你要购买的物品(输入0退出): ").strip())
                    if inp > 0 and inp <= len(all_shop_card):
                        if all_shop_card[inp - 1].name != "卖完了" and game.gold >= all_shop_card[inp - 1].rarity:
                            game.gold -= all_shop_card[inp - 1].rarity
                            game.all_card.append(Card(all_shop_card[inp - 1].card_id))
                            all_shop_card[inp - 1].name = "卖完了"
                        else:
                            print("你没有足够的金币或者已卖完")
                    elif inp == 0:
                        try:
                            os.system("cls")
                            print("确认退出？")
                            inp = int(input("1.确认\n2.取消\n").strip())
                            if inp == 1:
                                break
                            elif inp == 2:
                                continue
                        except ValueError:
                            continue
                except ValueError:
                    continue
        # 打开宝箱
        elif list_[0] == -3:
            from ...common.relic import Relic
            from ....start_game import Game
            relic_file_path = r'data\al_relic.json'
            with open(relic_file_path, 'r', encoding='utf-8') as f:
                relic_data: dict = json.load(f)
            al_relic_ = [relic for relic in relic_data.keys() if len(relic) >= 4]
            relic_3: list[Relic] = []
            for i in range(3):
                ii = random.choice(al_relic_)
                relic_3.append(Relic(ii))
                al_relic_.remove(ii)
                
            while True:
                os.system("cls")
                i1 = 1
                for i in relic_3:
                    print(f"{i1}: {i.name}")
                    i1 += 1
                    
                try:
                    inp = int(input("请选择一个遗物: ")) - 1
                except ValueError:
                    continue
                if inp >= 0 and inp < len(relic_3):
                    game.relic.append(relic_3[inp])
                    break

    # 运行对话
    def run(self, game):
        from ....start_game import Game
        game: Game = game
        log_dict = self.dialogue_list[0]
        os.system("cls")
        while True:
            print(log_dict['question'])
            ii = 1
            for i in log_dict['options']:
                print(f"{ii}. {i}")
                ii += 1
            inp = 0
            while True:
                try:
                    inp = int(input("请输入选项: ").strip())
                except ValueError:
                    inp = -1
                if len(log_dict["trigger"]) == 1 or (inp > 0 and inp <= len(log_dict["trigger"])):
                    break
                else:
                    print("输入错误,请重新输入")
            if log_dict['trigger'][str(inp)][0] != -2 and log_dict['trigger'][str(inp)][0] != -3:
                self.trigger(log_dict['trigger'][str(inp)], game)
            else:
                ft = self.trigger(log_dict['trigger'][str(inp)], game)
                if ft == -1:
                    break
            if log_dict['trigger'][str(inp)][-1] == -1:
                break
            else:
                log_dict = self.dialogue_list[log_dict['trigger'][str(inp)][-1]]
            os.system("cls")