from enum import Enum

class TypeActions(Enum) :
    REFRESH = 0
    RENAME_ALL = 1
    FUSE_WITH = 2
    CREATE_NEW_FOLDER = 3
    CLOSE_GROUP = 4
    RENAME_IN_ASCENDING_ORDER = 5
    BROWSE = 6
    RENAME_ALL_CATEGORIES = 7

# r = TypeActions["REFRESH"]
# print(type(r), r.name)

class Action() :
    def __init__(self, _type_action : TypeActions, _index : int, _value : any, _previous_datas : any) -> None:
        self.type = _type_action
        self.concernIndex = _index
        self.concernValue = _value
        self.datas = _previous_datas