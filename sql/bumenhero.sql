CREATE DATABASE bumen;
USE bumen;

#创建userinfo
CREATE TABLE userinfo (
  id INT PRIMARY KEY  AUTO_INCREMENT,
  username VARCHAR(20) NOT NULL ,
  nickname VARCHAR(20) NOT NULL ,
  password VARCHAR(20) NOT NULL ,
  trade_no VARCHAR(50) NOT NULL ,
  bubi_address VARCHAR(50) NOT NULL ,
  myset VARCHAR(100) NOT NULL ,
  statu INT(2) NOT NULL

);

CREATE TABLE assetsentinfo(
  id INT PRIMARY KEY AUTO_INCREMENT,
  from_bubi_address VARCHAR(20) NOT NULL ,
  to_bubi_address VARCHAR(20) NOT NULL ,
  trade_no_asset VARCHAR(20) NOT NULL
);

CREATE TABLE assetcreateand(
  id INT PRIMARY KEY AUTO_INCREMENT,
  assetname VARCHAR(20) NOT NULL ,
  assetcode VARCHAR(50) NOT NULL ,
  asset_issuer VARCHAR(50) NOT NULL ,
  bc_hash VARCHAR(50) NOT NULL ,
  asset_amount INT NOT NULL
)


# UPDATE userinfo SET password = "6473883" ,trade_no = "12313131" WHERE bubi_address = "bubiV8i7jAPmVsPo5FQ8qfH8KHP5bG2kMtURUDij";