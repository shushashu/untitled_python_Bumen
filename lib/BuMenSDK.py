#!/usr/bin/python
# -*- coding:utf-8 -*-

from urllib import parse, request
import ssl, time, datetime, json, requests, random, hashlib
from functools import wraps

__url__ = "https://testapi.bumeng.cn/"
__client_id__ = "1d60edfa67af7e1ce4ac1dab40577e6c"
__client_secret__ = "803da2e4d8a8b96726c96a04b912b5b5"
__log__ = True


# 构造一个trade_no
# 当下时间戳+时间戳和时间戳的2倍之间的随机数之后，补齐25位唯一tradeNum
def createTradeNo(type):
    if not isinstance(type, str):
        return "参数类型错误"
    T = int(time.time())
    R = int(random.randint(T, T + T))
    trade_no = type + str(T) + "x" + str(R)
    return trade_no.zfill(32)


# 日志
def writelog(*params):
    T = str(datetime.datetime.today())
    logfilename = T[0:10] + "userdata.log"
    writelog = T + str(params) + "\n"
    with open(logfilename, 'a+') as load_f:
        logfile = load_f.write(writelog)
    return logfile


# 玩家数据：目前使用json数据保存
# 写入用户数据：2个参数，参数1是username，参数2是userdata{}
# 读取玩家数据：不传入参数即可
def userDataIO(*params):
    if len(params) > 1:  # 插入新增玩家数据
        # 把玩家数据从文件中读出
        with open("userdate.json", "r") as load_f:
            loadfile = load_f.read()
            if not (len(loadfile) > 0):
                loadfile = dict()
            else:
                loadfile = json.loads(loadfile)
            # 新增的用户数据合并用户原有数据中
            key, value = params[0], params[1]
            loadfile = dict(loadfile, **{key: value})
        with open("userdate.json", "w") as load_f:
            # return load_f.write(json.dumps(loadfile))
            return load_f.write(json.dumps(loadfile))

    elif len(params) == 0:  # 读取玩家数据
        with open("userdate.json", "r") as load_f:
            loadfile = load_f.read()
        return json.loads(loadfile)
    else:
        return "参数错误"


# md5签名
def rnMD5(*params):
    stringA = ("asset_amount=%s&asset_code=%s&current_string=%s&from_bubi_address=%s&to_bubi_address=%s&trade_no=%s" % (
        params[0]["asset_amount"], params[0]["asset_code"], params[0]["current_string"], params[0]["from_bubi_address"],
        params[0]["to_bubi_address"], params[0]["trade_no"]))
    stringA = stringA + ("&key=%s" % __client_secret__)
    # stringA = "asset_amount=1&asset_code=2UX4xvQ4aWzemiS3R2FfWeyLdHDhbzzwitPcJHoPtAC5ZA2en5dxMhyagPyHxKLZZXCQYobP2W87KRjP3QyjPkbX5F28WUCLVZSGMt4mD4n5T7d9QwVaCd9Z6ZoTRS4fbi5e3SVmFLbmu96i&current_string=0000000000000001522052770147user&from_bubi_address=bubiV8hv8d7vBDeyrui8KiLmE4EU4id4UoQ1UKRu&to_bubi_address=bubiV8iDawDHmNdnZ9qwKy2cL6jeCN1SbCsuiVhV& trade_no=00000000001522052775784assetSend&key=privbxxXe9MLSFuxAfSePhVZYKxbGwgrNfnNTFjGxXs46GtMUMg47KCg"
    stringA = stringA.encode(encoding='utf-8')
    m2 = hashlib.md5()
    m2.update(stringA)
    # print("stringA",stringA,m2.hexdigest())
    return m2.hexdigest()


# 创建全局唯一票据号
def access_Token():
    grant_type = "client_credentials"
    urlAccessToken = __url__ + "/oauth2/token"
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    postData = {'client_id': __client_id__, 'client_secret': __client_secret__, 'grant_type': grant_type}
    # ssl._create_default_https_context = ssl._create_unverified_context
    req = requests.post(urlAccessToken, params=postData, headers=header, verify=False)
    # print(req.url)
    return req.json()["access_token"]


def access_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs["token"] = access_Token()
        # print(kwargs["token"])
        return func(*args, **kwargs)

    return wrapper


# 装饰器创建trade_no
def Ttrade_no(type):
    def trd(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs["trade_no"] = createTradeNo(type)
            return func(*args, **kwargs)

        return wrapper

    return trd


# 创建用户
# 使用需要传入用户用户名和用户密码，还有其他的待验证数据
# UserData =  {
#     "user_name": username,
#     "password": password,
#     "trade_no":trade_no
# }

@access_token
@Ttrade_no("user")
def createUser(user_name, nickname, password, trade_no, metadata, token):
    userdate = {
        "user_name": user_name,
        "password": password,
        "trade_no": trade_no,
        "metadata": metadata + "&nickname=" + nickname
    }
    print(userdate, token)
    urlCreateUser = __url__ + "/account/v1/register?access_token=" + token
    req = requests.post(urlCreateUser, json=userdate, verify=False)
    return req.json(), writelog(userdate["trade_no"], req.json())


# 查询账户注册状态
@access_token
def selectIsUser(trade_no, token):
    urlselectuser = __url__ + "/status/account/v1/register?access_token=" + token
    token["trade_no"] = trade_no
    req = requests.get(urlselectuser, params=token, verify=False)
    return req.json(), writelog(trade_no, req.json())


# 重置账户
# data={
# 	"user_name":"1520224496",
# 	"new_password":"gmc2188195",
# 	"trade_no":trade_no
# }
@access_token
def resetUser(token, data):
    urlresetuser = __url__ + "/account/v1/alterPwd?access_token=" + token
    req = requests.post(urlresetuser, json=data, verify=False)
    return req.json(), writelog(data["trade_no"], req.json())


# 获取账户信息
@access_token
def getUser(user_bubi_address, token):
    # access_token=access_Token()
    urlgetuser = __url__ + "/account/v1/info"
    token["bubi_address"] = user_bubi_address
    req = requests.get(urlgetuser, params=token, verify=False)
    return req.json(), writelog(req.json())


# 同步发行资产:
# assetdata={
# 		"trade_no":"10000098918373515766",
# 		"asset_issuer":"bubiV8i4dAC7GG59xXFTqPY7uuoMBTHSv7AvtNr5",
# 		"password":"gmc2188195",
# 		"asset_name":"绿耳朵资产",
# 		"asset_unit":"朵",
# 		"asset_amount":"21300",
# 		"metadata": "{\"asset_type\":\"10600\",\"asset_unit_code\":\"15\",\"asset_description\":\"xxxxxxxxxxx\"}"
# 	}
@access_token
def assetCogradient(assetdata, token):
    urlasset = __url__ + "/asset/v1/issue"
    req = requests.post(urlasset, params=token, json=assetdata, verify=False, )
    return req.json(), writelog(assetdata["trade_no"], req.json())


# 查询资产详情
@access_token
def assetSelect(asset_code, token):
    url_asset_select = __url__ + "/asset/v1/showDetail"
    token["asset_code"] = asset_code
    req = requests.get(url_asset_select, params=token, verify=False)
    return req.json(), writelog(req.json())


# 查询资产发行状态
@access_token
def assetIssue(trade_no, token):
    url_asset_issue = __url__ + "/status/asset/v1/issue"
    token["trade_no"] = trade_no
    req = requests.get(url_asset_issue, params=token, verify=False)
    return req.json(), writelog(trade_no, req.json())


# 同步增发资产
# data={
# 	"password": "gmc2188195",
# 	"trade_no": trade_no,
# 	"asset_code": "2UX4xvQ4aX18qxFaXjn9qsDwVE8AKLD2r72d8fCSTWbSp7gyUvarRWPvU5q79BS2WibcYSi17THrCnNs8JJwRn1YgLiW4n9Z4DcUDbAHAAQ4gSr8GZiA5xqynQxP8EP2PLhgmULW4yeaqjrq",
# 	"asset_amount": "10000",
# 	"metadata": "{\"asset_type\":\"10600\",\"asset_unit_code\":\"15\",\"asset_description\":\"闪避狂暴甲\"}"
# }
@access_token
def assetAdd(token, data):
    url_asset_add = __url__ + "/asset/v1/add2Issue"
    req = requests.post(url_asset_add, params=token, json=data, verify=False)
    return req.json(), writelog(data["trade_no"], req.json())


# 资产同步转移
# data={
# "trade_no" : trade_no,
# 	"current_string" : "MqUq6TASQju57VcH",
# 	"password" : "gmc2188195",
# 	"asset_code" : "2UX4xvQ4aX18qxFaXjn9qsDwVE8AKLD2r72d8fCSTWbSp7gyUvarRWPvU5q79BS2WibcYSi17THrCnNs8JJwRn1YgLiW4n9Z4DcUDbAHAAQ4gSr8GZiA5xqynQxP8EP2PLhgmULW4yeaqjrq",
# 	"asset_amount" : "240",
# 	"from_bubi_address" : "bubiV8hzgJQG16bFsuN5YUfr18sTiUjqiPEkyEew",
# 	"to_bubi_address" : "bubiV8i4iUouxQwJNKRkpJNiGZ8nKUX7SRnsnm4G",
# 	"metadata" : "{\"sub_tx_type\":\"10100\"}",
# 	"sign" : "kfB53Q4aSJmDLyKguiP6mG5bee2XmtbTNQ2"#签名
# }
@access_token
def assetSent(token, data):
    url_asset_sent = __url__ + "/asset/v1/send"
    data["sign"] = rnMD5(data)
    # print(data)
    req = requests.post(url_asset_sent, params=token, json=data, verify=False)
    return req.json(), writelog(data["trade_no"], req.json())


# 资产转移状态查询
@access_token
def assetSentIsure(token, trade_no):
    url_asset_sent_Issure = __url__ + "/status/asset/v1/send"
    token["trade_no"] = trade_no
    req = requests.get(url_asset_sent_Issure, params=token, verify=False)
    return req.json(), writelog(trade_no, req.json())
