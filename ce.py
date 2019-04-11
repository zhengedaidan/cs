import re
# findall = re.findall(r'q(.*?)a','q\n66a')
# print(findall)
#
#
# search = re.search(r'(\s)8(\s)','9 8 ')
# print(search.group(1),search.group(2),end='')


# def show(match_obj):
#     ret = match_obj.group()
#     print(ret)
#     return "哈哈哈" + ret
# result = re.sub(r"\d+",show,"阅读100")
# print(result)

str = 'qweq'
str = "srt"
print([str])
print([str.replace('\'', '\"')])

ret1 = re.sub(r'q','\"',str)
print([ret1])

