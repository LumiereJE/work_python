# 인덱싱과 슬라이싱

jumin = "901120-1234567"

gender = jumin[8]           # 성별
year = jumin[:2]            # 출생년도
month  = jumin[2:4]         # 월, 2번인덱스 4번인덱스 미만
day = jumin[4:6]            # 일

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : "+ jumin[7:])
print("뒤 7자리 : "+ jumin[-7:])








