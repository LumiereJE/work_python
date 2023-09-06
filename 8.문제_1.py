# 1번문제 - 정해진 형식으로 시간을 입력 받아서 출력하기
#          입력 형식      22:5:5 → 오후 10시 05분 05초

# hour, min, sec = map(int,input("시간 입력 : ").split(":"))
# if(hour > 12):
#     hour -= 12
#     print(f"오후 {hour:00}시 {min:00}분 {sec:00}초")
# else:
#     print(f"오전 {hour:00}시 {min:00}분 {sec:00}초")



# 2번문제 - 3개의 정수를 입력 받아 최대값과 최소값 구하기

# num1, num2, num3 = map(int,input("숫자 3가지 입력:").split())
#
# if num1 > num2 | num3 :
#     print(num1)
# else if num2 > num1 | num3 :
#     print(num2)

# 3번문제 - 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
from datetime import datetime

curr_year = datetime.today().year
info = input("주민등록 번호를 입력하세요(-제외) : ")

year = int(info[:2])
month = int(info[2:4])
day = int(info[5:7])
gender = int(info[7])
old = curr_year - 2000 - year

if gender == "1" or gender == "3":
    gender_str = "남성"
else:
    gender_str = "여성"


print(f"""
생년 월일 : {year}년 {month}월 {day}일
성별 : {gender_str}
나이 : {old}
""")


# 4번문제 - 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기
#          list를 사용해야.. 하 .. 는..ㄷ ㅔ..






