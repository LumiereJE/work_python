# 제어문 : 조건문 / 반복문
#         순차적인 흐름을 제어하는 목적으로 사용 됨.

# n = int(input("정수를 입력 하세요 : "))
#
# if n > 100:
#     print(f"{n}은 100보다 커요")
# elif n < 100:
#     print(f"{n}은 100보다 작아요")
# else:
#     pass    # else구문 비우면 오류임

# 조건문 - 문자열 비교
while True :
    season = input("현재 계절을 입력하세요 : ")
    if season == "spring":
        print("봄이 왔어요")
        break
    elif season == "summer":
        print("더운 여름입니다.")
        break
    elif season == "fall" or season =="autumn":
        print("가을이 왔어요.")
        break
    elif season == "winter":
        print("추운 겨울이 왔어요.")
        break
    else:
        print("계절을 잘못 입력 하셨습니다.")





