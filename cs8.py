# -*- coding:utf-8 -*-
import io
from ruamel.yaml import round_trip_dump,round_trip_load_all,round_trip_load,safe_dump,safe_dump_all,safe_load
def dump_yaml_file(path,round_trip=False):
    # with io.open(path) as reader:
    #     cs_data=round_trip_load_all(reader)
    #     print(cs_data)
    with open(path,"r",encoding="utf-8") as reader:
        # cs_data=round_trip_load(reader)
        cs_data=safe_load(reader)
        print(cs_data)
        # print(dict(cs_data))
        for i in cs_data[0].items():
            print(i)
dump_yaml_file("folder/y7.yaml",True)

import json
d={"aa":11}
print(json.dumps(d))
print(type(json.dumps(d)))