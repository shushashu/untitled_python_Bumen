import BuMenSDK,time
import mysql

class user(object):


	__trade_no = BuMenSDK.createTradeNo("user")


	def __init__(self,username,password,metadata,**kwargs):
		self.username = username
		self.password = password
		self.metadata = metadata

	def create_user(self):
		###账户相关
		# 创建用户并把用户数据写入本地文件
		return

	def selectIsUser(self):
		# 查询用户注册状态
		return



# 创建用户
class createuser(user):


	__sql = "INSERT INTO userinfo (nickname, password, trade_no, bubi_address,myset,username,statu) VALUES ( %s, %s, %s,%s,%s, %s,%s )"

	def __init__(self,trade_no,token,username,password,metadata,nickname, **kwargs):
		user.__init__(self,username,password,metadata,**kwargs)
		self.nickname = nickname
		self.trade_no = trade_no
		self.token= token

	def create_user(self):
		userdata = {
			"user_name": self.username,
			"password": self.password,
			"trade_no": self.trade_no,
			"metadata": self.metadata,
		}
		self.a = BuMenSDK.createUser(userdata, self.token)
		return int(self.a[0]["err_code"])


	def sql(self):
		data = (
			self.nickname,
			self.password,
			self.trade_no,
			self.a[0]["data"]["bubi_address"],
			self.metadata,
			self.username,
			self.status
		)
		s = mysql.mysql(sql=self.__sql, data=data)
		return s.insert()


	def selectIsUser(self):
		# 查询用户注册测状态
		if BuMenSDK.selectIsUser(self.trade_no,self.token)[0]["err_code"] == "0":
			self.status = 1
		else:
			self.status = 0
		return self.status


trade_no = BuMenSDK.createTradeNo("user")
token = BuMenSDK.access_Token()
username,password,metadata,nickname = "test021","123123","iammetadata","nick021"

user1 = createuser(trade_no,token,username,password,metadata,nickname)

a = user1.create_user()
if a == 0 :
	b = user1.selectIsUser()
	if b == 1:
		c = int(user1.sql())
		if c <= 0:
			print("数据库存储错误")
	else:
		print("user1.selectIsUser()",a)
else:
	print("user1.create_user()",a)


# if type(user1.create_user()) == str:
# 	print(type(user1.selectIsUser()),user1.selectIsUser(),user1.create_user())
# 	if user1.selectIsUser()["err_code"] == 0:
# 		user1.status = 1
# 		print(user1.sql())





	#  nickname VARCHAR(20) NOT NULL ,
	#   password VARCHAR(20) NOT NULL ,
	#   trade_no VARCHAR(50) NOT NULL ,
	#   bubi_address VARCHAR(20) NOT NULL ,
	#   myset VARCHAR(50)

	#查询用户：
	# print(BuMenSDK.userDataIO())

	#查询用户注册状态
	# token=BuMenSDK.access_Token()
	# userdata=BuMenSDK.userDataIO()["1520254732"]
	# a=BuMenSDK.selectIsUser(userdata["trade_no"],token)
	# print(a)

	# #查询用户详情
	# token=BuMenSDK.access_Token()
	# userdata=BuMenSDK.userDataIO()["1520254732"]
	# a=BuMenSDK.getUser(userdata["bubi_address"],token)
	# print(a)

	# 重置账户

	# token = BuMenSDK.access_Token()
	# trade_no = BuMenSDK.createTradeNo("user")
	# data = {
	#     "user_name":"17625975662",
	# 	"new_password":"123456",
	# 	"trade_no":trade_no
	#
	# }
	# a = BuMenSDK.resetUser(token=token,data=data)
	# print(a)