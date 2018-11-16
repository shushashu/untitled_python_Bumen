from lib import BuMenSDK
from userinfo import user

# 配置用户数据
username, password, metadata, nickname = "test0245", "123123", "iammetadata", "nick032"

# 创建用户
user1 = user.CreateUser(username, password, metadata, nickname)

# 检查用户创建结果
a = user1.create_user()
if a == 0:
    b = user1.selectIsUser()
    print("user1.selectIsUser()", a)
    print(b)
else:
    print("user1.create_user()", a)
