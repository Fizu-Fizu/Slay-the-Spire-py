# 练习项目 - 杀戮尖塔  
## 项目介绍
- 本项目为个人练习项目，玩法完全基于 **《杀戮尖塔》**，用Python语言编写，终端游玩，目前还在开发。
- ~~本人鱼脑，此日志防止我第二天看不懂了~~(划掉)
## 项目结构:  
```
Slay the Spire-py/
├── .gitignore
├── main.py
├── map.txt
├── README.md
├── data/
│   ├── al_buff.json
│   ├── al_card.json
│   ├── al_dialogue.json
│   ├── al_object.json
│   └── al_relic.json
└── src/
    ├── start_game.py
    ├── __init__.py
    └── game/
        ├── __init__.py
        ├── cards/
        │   ├── card.py
        │   ├── is_playing.py
        │   └── __init__.py
        ├── common/
        │   ├── buff.py
        │   ├── relic.py
        │   └── __init__.py
        ├── core/
        │   ├── intent.py
        │   ├── object.py
        │   └── __init__.py
        └── map/
            ├── map.py
            ├── node.py
            ├── __init__.py
            └── room/
                ├── battle_time.py
                ├── dialogue.py
                ├── dialogue_trigger.py
                ├── room.py
                └── __init__.py
```  
### 0.0 创建项目  
#### 1.关于cards:
- **卡牌定义**：通过`Card`类实现，包含卡牌ID、名称、能量消耗、类型（攻击/技能/能力/状态）、效果数据等属性
- **卡牌效果**：攻击牌（类型1）支持基础伤害计算与AOE效果，技能牌（类型2）预留格挡与Buff逻辑框架，其他暂未实现
- **数据配置**：卡牌数据存储于`data/al_card.json`
#### 2.关于common:
- **Buff**：通过`Buff`类实现，包含BuffID、名称、效果数据等属性，通过`trigger_damage`和`trigger_block`函数处理Buff对伤害/格挡的增减效果
- **遗物**：通过`Relic`类实现，包含遗物ID、名称、遗物效果数据等属性
- **数据配置**：数据存储于`data/al_relic.json`和`data/al_buff.json`，都拥有相当多的bool属性，用于控制Buff/遗物触发时机
#### 3.关于core:
- **敌方意图**: 通过`Intent`类实现，包含技能ID、名称、意图数据等属性，意图会在我方回合结束触发
- **对象**：通过`Object`类实现，包含对象ID、名称、血量数据等属性，这个是敌方目标的基础类
#### 4.关于map:
- **地图**：通过`Map`类实现，包含地图ID、名称、地图数据等属性，地图会生成一个二维数组，用于存储地图信息
- **房间**：通过`Room`类实现，房间指战斗房间，这个类里包含了玩家数据、敌方数据和卡牌数据
- **节点**：通过`Node`类实现，节点指地图上的一个格子，节点会根据属性不同触发对应效果，通过图标区分7种节点（`["💀","💰","🔥","👻","😈","💎","❓"]`），对应Boss、商店、休整点等场景  
### 0.1 更新内容  
- 整理了文件结构
- 添加了data文件夹来统一存储数据
- src用来存储项目源代码
- 优化了ImportError，现在是可以运行的，但只能查看地图生成情况