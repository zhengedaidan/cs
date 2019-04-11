# -*- coding:utf-8 -*-
from jinja2 import Environment,FileSystemLoader
j2_env=Environment(loader=FileSystemLoader("template"))
j2_tem=j2_env.get_template("py.j2")
model=j2_tem.render(b="好",c="坏")
print(model)