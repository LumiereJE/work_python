# 회원정보를 입력받아서 출력하기

# 이름
# 나이 : 1 ~ 199까지. 그 외는 재입력 요청.
# 성별 : M, m은 남성 / F, f는 여성  그 외는 재입력 요청.
# 직업 : 1(학생) 2(회사원) 3(주부) 4(무직)  외에는 재입력 요청.
# 결과는 한번에 출력

name = input("이름 : ")
age = int(input("나이 : "))
gender = input("성별(M,m / F,f) : ")
jobs = input("직업 - 1(학생) 2(회사원) 3(주부) 4(무직) : ")



if 0 < age < 200:
    pass
else:
    print("나이 범위를 벗어났습니다.")

while gender:
    if gender == "M" or gender == "m":
        gender = "남성"
        break
    elif gender == "F" or gender == "f":
        gender = "여성"
        break
    else:
        print("나이를 다시 선택해주세요.")




while jobs:
    if jobs == "1":
        jobs = ("학생입니다.")
        break
    elif jobs == "2":
        jobs = ("회사원입니다.")
        break
    elif jobs == "3":
        jobs = ("주부입니다.")
        break
    elif jobs == "4":
        jobs = ("무직입니다.")
        break
    else:
        print("직업을 다시 선택해주세요.")
        break


print(f"{name}님은 {age}세, {gender}이고, {jobs}")




