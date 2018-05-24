# -*- coding:utf-8 -*-
# import json
# import requests
# from base import BossTest
#
#
# class DepartrueAppro(BossTest):
#     def __init__(self):
#         self.token_headers, _ = self.auth_login('13166326930')
#         super(DepartrueAppro, self).__init__()
#     def cs(self):
#         req = requests.post('http://127.0.0.1:8081/1.0/account/is_departure_approver',
#                             headers=self.token_headers)
#         if req.ok:
#             print json.dumps(json.loads(req.text.encode("utf8")))
#         else:
#             print 'faillllll'
# DepartrueAppro().cs()



import bson
print(bson)