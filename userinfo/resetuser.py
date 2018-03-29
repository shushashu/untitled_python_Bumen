from lib import BuMenSDK
from userinfo import user

# 重置账户所需的参数
username = "test027"
password = "678975765"
token = BuMenSDK.access_Token()
trade_no = BuMenSDK.createTradeNo("user")


re = user.resetuser(trade_no=trade_no, token=token["access_token"], username=username, password=password)
a = re.resetuser()
if a["err_code"] == "0":
    re.sql()
else:
    print(a["err_code"])