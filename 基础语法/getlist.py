# @Time : 2020/11/12 10:17
# @Author : WZG
# --coding:utf-8--

a = {'code': 0, 'message': None, 'data': {'list': [{'id': 97, 'organizationId': 1, 'organizationName': '智慧用电', 'roleId': 98, 'roleName': '二把手', 'photoId': '', 'username': 'hhhhhhhh', 'name': 'hhhhh', 'sex': 0, 'phone': '17633501171', 'email': '', 'description': '', 'status': False, 'addTime': 1605144708, 'updateTime': 1605144708, 'expireTime': 1636680675, 'expireStatus': 0}], 'total': 1}, 'success': True, 'resultCode': 'SUCCESS'}
print(a['data']['list'][0]['id'])