content = b'x\x9c\xabV*J-Q\xb2RP\n)*MU\xd2QP*\xc9\xccM\x05\xf1\x8d\x0c\r\xcc\x8d\x0c\r\xc1X\xcf\xc2\xc0\xd4\xdc\xd2X\xa9\x16\x00"\x8b\x0bq'
print(type(content))
print(content.decode('euc-kr','ignore'))
print(content.decode('utf-8','backslashreplace'))
print(content.decode('utf-8','replace'))
