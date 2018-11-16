from lib import mysql
from lib import BuMenSDK


class User(object):
    __status = ""

    def __init__(self, trade_no, token, username, password, **kwargs):
        self.username = username
        self.password = password
        self.trade_no = trade_no
        self.token = token

    def create_user(self):
        ###账户相关
        # 创建用户并把用户数据写入本地文件
        return

    def selectIsUser(self):
        # 查询用户注册状态
        return

    def resetuser(self):
        # 账户重置
        return

    def selectUserInfo(self):
        # 查询用户注册状态
        return


# 创建用户
class CreateUser(User):
    __sql = "INSERT INTO userinfo (nickname, password, trade_no, bubi_address,myset,username,statu) VALUES ( '{}', '{}', '{}','{}','{}', '{}','{}' )"

    def __init__(self, trade_no, token, username, password, metadata, nickname, **kwargs):
        super().__init__(trade_no=trade_no, token=token, username=username, password=password, **kwargs)
        self.nickname = nickname
        self.metadata = metadata

    def create_user(self):
        userdata = {
            "user_name": self.username,
            "password": self.password,
            "trade_no": self.trade_no,
            "metadata": self.metadata,
            "nickname": self.nickname,
        }
        self.a = BuMenSDK.createUser(token=self.token, **userdata)
        return int(self.a[0]["err_code"])

    def sql(self):
        sql = self.__sql.format(
            self.nickname,
            self.password,
            self.trade_no,
            self.a[0]["data"]["bubi_address"],
            self.metadata,
            self.username,
            self.__status
        )
        s = mysql.mysql(sql)
        return s.insert()

    def selectIsUser(self):
        # 查询用户注册测状态
        if BuMenSDK.selectIsUser(self.trade_no)[0]["err_code"] == "0":
            self.__status = 1
        else:
            self.__status = 0
        return self.__status


# 账户重置
class ResetUser(User):
    __sql = 'UPDATE userinfo SET password = "{}" ,trade_no = "{}" WHERE username = "{}"'
    __status = ""

    def __init__(self, trade_no, token, username, password, **kwargs):
        super().__init__(trade_no=trade_no, token=token, username=username, password=password, **kwargs)

    def resetuser(self):
        data = {
            "user_name": self.username,
            "new_password": self.password,
            "trade_no": self.trade_no,
        }
        a = BuMenSDK.resetUser(token=self.token, data=data)
        return a[0]

    def sql(self):
        sql = self.__sql.format(
            self.password,
            self.trade_no,
            self.username
        )
        s = mysql.mysql(sql)
        return s.update()

# 查询用户注册状态
# token=BuMenSDK.access_Token()
# userdata=BuMenSDK.userDataIO()["1520254732"]
# a=BuMenSDK.selectIsUser(userdata["trade_no"],token)
# print(a)

# #查询用户详情
# token=BuMenSDK.access_Token()
# userdata=BuMenSDK.userDataIO()["1520254732"]
# a=BuMenSDK.getUser(userdata["bubi_address"],token)
# print(a)
