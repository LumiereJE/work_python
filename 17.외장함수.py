# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함

import random
# random 넣으면 값이 순서대로 안나옴.
# randint(0, 4) → 0 ~ 4 이하의 임의의 정수값이 반환됨
# randrange(0, 4) : 0 ~ 4 미만의 임의의 정수값이 반환됨


# for i in range(100):
#     rand = random.randint(0, 4)
#     print(rand)

# 현재시간 가져오기
# import datetime만 해두면 나중에 datetime.datetime.today() 라고 사용해야 함
from datetime import datetime   # datetime 모듈에서 datetime함수만 import 함
print(datetime.today())                # 현재 날짜 가져옴
print(datetime.today().year)           # 현재 연도 가져옴
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 수학 계산을 위한 math
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))            # 로그값
print(math.ceil(100.1))         # 올림 (반올림x)
print(math.floor(100.1))        # 내림 (반올림x)

# list → 터미널에 pip list 입력해서 설치
#        install simple-colors      하면 simple-colors 설치됨

# 중복값이 없는 로또 번호 생성하기
import random
print("로또 번호 자동 생성기")
ls = []                         # 빈 리스트 만들기. ()로 만들면 튜플됨
while True:
    rand = random.randrange(1, 46)
    if rand not in ls:      # list에 생성된 rand값이 포함되어 있지 않으면
        ls.append(rand)     # 번호 추가
    if len(ls) == 6: break  # 숫자 6개 들어가면 끝.
print(ls)













