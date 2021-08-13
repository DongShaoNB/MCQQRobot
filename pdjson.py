#  Copyright (c) 2020 - 2021 DongShaoNB
#  该代码由DongShaoNB创建
#  由DongShaoNB一人编写
#  版权归DongShaoNB所有!
import json


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
