# # -*- coding:utf-8 -*-
# from pprint import pprint
from datetime import datetime,timedelta
from pymongo import MongoClient
coon=MongoClient(host="192.168.1.133")
client=coon["boss"]["oa_examine_order"]
client1=coon["boss"]["oa_apply_order"]
from bson import ObjectId

def oa_cost(y=None,m=None):
    oa_cost_rents=[]
    oa_cost_others=[]
    if y is None:
        y = datetime.now().year
    if m is None:
        m = datetime.now().month
    d = datetime.now().day
    rent_cost_cusor = client1.find({"examine_state": {"$ne": -1}, "costclass_type":2,"created_at": ({"$gte": datetime(y,m,1)-timedelta(hours=8)})})
    result_rent=list(rent_cost_cusor)
    for i in result_rent:
        biz_id = i.get("cost_belong_items")[0].get("biz_id")
        # 只筛选成本归属为商圈的
        if biz_id:
            day_rent=i.get("month_rent")//30
            day_sub=(datetime(y, m, d)-datetime.strptime(i.get("contract_start_date"),"%Y-%m-%d")).days
            if day_sub >= 0:
                finally_rent=day_rent*(day_sub+1)
                oa_cost_rents.append({biz_id:finally_rent})
    other_cost_cusor=client1.find({"examine_state": {"$ne": -1}, "costclass_type":1,"created_at": ({"$gte": datetime(y,m,1)-timedelta(hours=8)})})
    result_other=list(other_cost_cusor)
    for j in result_other:
        biz_id = j.get("cost_belong_items")[0].get("biz_id")
        if biz_id:
            total_money=j.get("total_money")
            oa_cost_others.append({biz_id:total_money})

    oa_cost_rents.extend(oa_cost_others)
    return_dict={}
    for i in oa_cost_rents:
        if list(i.keys())[0] in return_dict:
            return_dict[list(i.keys())[0]] = (return_dict[list(i.keys())[0]] + list(i.values())[0])
        else:
            return_dict[list(i.keys())[0]] = list(i.values())[0]
    print(return_dict)


oa_cost(y=2018,m=5)










    # apply_order_ids=[]
    # for i in result_day:
    #     for j in i.get("apply_order_list"):
    #         apply_order_ids.append(j)
    # print("满足条件的申请单～～",apply_order_ids)


    # rent_moneys=[]
    # other_moneys=[]
    # for i in apply_order_ids:
    #     for j in client1.find({"_id":ObjectId(i)}):
    #         # 租房
    #         if j.get("costclass_type")==2:
    #             #日租金
    #             day_rent=int(j.get("month_rent")/30)
    #             #起租日期
    #             contract_start_date=j.get("contract_start_date")
    #             #起租和今天0点相差的天数
    #             start_now_sub=(datetime.strptime(contract_start_date,"%Y-%m-%d")-datetime(y, m, d-1,18)).days
    #             if start_now_sub>=0:
    #                 rent_moneys.append(day_rent*(start_now_sub+1))
    #         else:
    #             other_money=j.get("total_money")
    #             other_moneys.append(other_money)
    # print("今天租房的费用～～",rent_moneys)
    # print("今天报销的费用～～",other_moneys)


# def cs(self, phone):
#     self.token_headers, _ = self.auth_login(phone)
#     req = requests.post('http://127.0.0.1:8081/1.0/account/or_approve_leave', headers=self.token_headers)
#     print
#     req.content.decode()