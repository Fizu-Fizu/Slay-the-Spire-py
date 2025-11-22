class Dialogue:
    # 事件ID
    dialogue_id: int
    # 事件名称
    dialogue_name: str
    # 事件内容
    dialogue_list: list[dict] = []
    # 事件类型 ： 1、Info信息展示,2、Choice事件选择,3、Confirm二次确认(高风险)||辅助类型4+
    dialogue_type: int = 0

    def __init__(self, dialogue_id: int):
        1