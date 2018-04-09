# -*- coding:utf-8 -*-
import os
import glob
import ruamel.yaml
i=1
for filepath in filter(os.path.isfile,glob.glob("folder/*")):
    filedir=os.path.dirname(filepath)
    print(filedir)

    # with open(os.path.join(filedir+"/"+str(i)),"w") as f:
    with open(filedir+"/"+str(i),"w") as f:
        f.write("111")
        i+=1






