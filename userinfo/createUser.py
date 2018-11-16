from lib import BuMenSDK
from userinfo import user

# 配置用户数据
trade_no = BuMenSDK.createTradeNo("user")
token = BuMenSDK.access_Token()
username, password, metadata, nickname = "test0235", "123123", "iammetadata", "nick032"

# 创建用户
user1 = user.CreateUser(trade_no, token, username, password, metadata, nickname)

# 检查用户创建结果
a = user1.create_user()
if a == 0:
    b = user1.selectIsUser()
    if b == 1:
        c = int(user1.sql())
        if c <= 0:
            print("数据库存储错误")
    else:
        print("user1.selectIsUser()", a)
else:
    print("user1.create_user()", a)
