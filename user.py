import BuMenSDK,time

####账户相关
# 创建用户并把用户数据写入本地文件
# username=str(int(time.time()))
# token=BuMenSDK.access_Token()
# trade_no=BuMenSDK.createTradeNo("user")
# userdata={
# 	"user_name":username,
# 	"password":username,
# 	"trade_no":trade_no
# }
# a=BuMenSDK.createUser(userdata,token)
# userd=a[0]
# userdata.update(userd["data"])
# userdata=BuMenSDK.userDataIO(userdata["user_name"],userdata)

#查询用户：
# print(BuMenSDK.userDataIO())

#查询用户注册状态
# token=BuMenSDK.access_Token()
# userdata=BuMenSDK.userDataIO()["1520254732"]
# a=BuMenSDK.selectIsUser(userdata["trade_no"],token)
# print(a)

#查询用户详情
token=BuMenSDK.access_Token()
userdata=BuMenSDK.userDataIO()["1520254732"]
a=BuMenSDK.getUser(userdata["bubi_address"],token)
print(a)