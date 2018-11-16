from lib import BuMenSDK
from userinfo import user

# 重置账户所需的参数
username = "test027"
password = "678975765"

re = user.ResetUser(username=username, password=password)
a = re.resetuser()
if a["err_code"] == "0":
    print(a)
else:
    print(a["err_code"])
