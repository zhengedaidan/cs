# -*- coding:utf-8 -*-
import io
import os
import glob
from ruamel.yaml import round_trip_dump, round_trip_load, safe_load, dump_all,dump

def load_yaml_file(path, round_tripping=False):
    with io.open(path, 'r', encoding='utf-8') as reader:
        pathdir=os.path.dirname(path)
        newfloder=pathdir+"copy"
        if not os.path.exists(newfloder): #判断文件夹是否存在
            os.mkdir(newfloder)
        if round_tripping:  #判断是否有注释
            data = round_trip_load(reader)
            # with open(newfloder+"/"+os.path.basename(path),"w",encoding="utf-8") as w:    拼接路径 加号方式需要有"/" join是逗号
            with open(os.path.join(newfloder,os.path.basename(path)),"w",encoding="utf-8") as wr:
                round_trip_dump(data, wr, allow_unicode=True)

        else:
            data = safe_load(reader)
            with open(os.path.basename(path),"w",encoding="utf-8") as wr:
                # dump(data, w, allow_unicode=True)
                dump_all([data], wr, allow_unicode=True)
    return data

if __name__ == '__main__':
    for filepath in filter(os.path.isfile, glob.glob("folder/*")):
        load_yaml_file(filepath,True)