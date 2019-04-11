# -*- coding:utf-8 -*-
# from jinja2 import Template
# template = Template('Hello {{ name }}!')
# print(template.render(name='World'))

# from jinja2 import Environment,PackageLoader,FileSystemLoader
# env = Environment(loader=FileSystemLoader('template', 'utf-8'))
# # env = Environment(loader=PackageLoader('tem',"temp",'utf-8'))
# # template = env.get_template('py.j2')
# template = env.get_template('my.html')
# print(template.render(b="模版变量"))

# di={"m":1}
# di.setdefault("n",{})["n"]=time.time()
# di.setdefault("p",{"p":time.time()})

s="23 1 4 ".replace(" ","")
print(s.isdigit())