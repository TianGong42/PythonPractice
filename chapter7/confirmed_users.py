'''
假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，
如何将他们移到另一个已验证用户列表中呢？一种办法是使用一个while循环，
在验证用户的同时将其从未验证用户列表中提取出来，再将其加入到另一个已验证用户列表中
'''
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
# 验证每个用户，直到没有未验证的用户为止
# 将每个经过验证的列表都移动到已验证用户列表中
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()
    print("验证用户:" + confirmed_user.title())
    confirmed_users.append(confirmed_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 整个套路就是把原来list里的东西取出来，放到现在的list里