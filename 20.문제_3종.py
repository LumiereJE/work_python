# 상근날드(초급) - 가장 싼 세트 구성의 가격 출력
# 세트메뉴 가격 = (버거단품 + 음료) - 50원
# 햄버거 - 상덕버거 중덕버거 하덕버거
# 음료 - 콜라 사이다

# menu = list(map(int, input("메뉴 가격 입력(공백 구분) : ").split()))
#
# burger = min(menu[:3])
# drink = min(menu[3:])
#
# print(burger + drink - 50)



# 저항(중급)
# color = {"black", "brown", "red", "orange",
#             "yellow", "green", "blue", "violet", "grey", "white"}

# color = "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"
#
# f_name = color.index(input())   # input()으로 입력받은 문자열이 color튜플안의 인덱스로 반환.  index로 묶어서 값의 번호 출력
# s_name = color.index(input())
# t_name = color.index(input())
#
# print(int(str(f_name)+str(s_name)) * (10 ** t_name))


# PC방 알바(중급)
# seat_num = list(map(int, input().split()))
# pc = [0] * 100          # 0으로 초기화된 100개의 리스트 생성
# cnt = 0
# for e in seat_num:      # 향상된 for문이니까 e값은 고객이 원하는 좌석 번호임.
#     if pc[e - 1] != 0: cnt += 1     # 좌석수는 1부터인데 배열은 0부터라서 -1 임.
#     else: pc[e - 1] = 1
# print(cnt)

seat_num = list(map(int, input().split()))
pc = [False] * 100          # 0으로 초기화된 100개의 리스트 생성
cnt = 0
for e in seat_num:      # 향상된 for문이니까 e값은 고객이 원하는 좌석 번호임.
    if pc[e - 1] False: cnt += 1     # 좌석수는 1부터인데 배열은 0부터라서 -1 임.
    else: pc[e - 1] = 1
print(cnt)

# Knuth-Morris-Pratt -> KMP, Mirko-Slavko -> MS
# upper_str = ""
# for e in input():      # 입력 받는 개수만큼 자동 순회
#     if e.isupper(): upper_str += e
# print(upper_str)

