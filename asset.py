import BuMenSDK

token=BuMenSDK.access_Token()

#资产发行和写入本地数据
# trade_no=BuMenSDK.createTradeNo("asset")
# userdata=BuMenSDK.userDataIO()["1520254732"]
# data={
# 		"trade_no":trade_no,
# 		"asset_issuer":userdata["bubi_address"],
# 		"password":userdata["password"],
# 		"asset_name":"城市",
# 		"asset_unit":"座",
# 		"asset_amount":"100",
# 		"metadata": {"asset_description":"拥有一座城市的玩家可以在城市做各种各样的事情，包括：战争（训练士兵，修筑防御，发动或者防御战争）；内政（组建政府，颁布政令，发展经济，毕竟有钱才能做更多的事情。）；培养英雄（不管是文官还是武将，都是城市发展成为帝国必不可少的助力，毕竟千军易得，一将难求）"}
# }
#
# a=BuMenSDK.assetCogradient(data,token)
# a[0]["data"]["asset_trade_no"]=trade_no
# userdata["asset"]=a[0]["data"]
# print(userdata)
# userdata=BuMenSDK.userDataIO(userdata["user_name"],userdata)#用户数据更新

#查询资产发行状态
# userdata=BuMenSDK.userDataIO()["1520254732"]
# trade_no=userdata["asset"]["asset_trade_no"]
# b=BuMenSDK.assetIssue(trade_no,token)
# print(b)

#查询资产详情
# userdata=BuMenSDK.userDataIO()["1520254732"]
# asset_code=userdata["asset"]["asset_code"]
# c=BuMenSDK.assetSelect(asset_code,token)
# print(c)

trade_no=BuMenSDK.createTradeNo("asset_sent")
userdata1=BuMenSDK.userDataIO()["1520254732"]
userdata2=BuMenSDK.userDataIO()["1520254735"]
data={
    "trade_no" : trade_no,
	"current_string" : "MqUq6TASQju57VcH",
	"password" : userdata1["password"],
	"asset_code" : userdata1["asset"]["asset_code"],
	"asset_amount" : "10",
	"from_bubi_address" : userdata1["bubi_address"],
	"to_bubi_address" : userdata2["bubi_address"],
	"metadata" : "{\"sub_tx_type\":\"10100\"}",
	"sign" : {}#签名
}
# BuMenSDK.assetIssue(trade_no,token)
a=BuMenSDK.assetSent(token,data)
b=BuMenSDK.assetSentIsure(token,trade_no)
c=BuMenSDK.assetSelect(data["asset_code"],token)
d=BuMenSDK.getUser(userdata1["bubi_address"],token)
e=BuMenSDK.getUser(userdata2["bubi_address"],token)
print(a)
print(b)
# print(c)
print(d)
print(e)

