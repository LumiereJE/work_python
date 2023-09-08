# 상근날드(초급) - 가장 싼 세트 구성의 가격 출력
# 세트메뉴 가격 = (버거단품 + 음료) - 50원
# 햄버거 - 상덕버거 중덕버거 하덕버거
# 음료 - 콜라 사이다

menu = list(map(int,input("메뉴 가격 입력(공백 구분) : ").split()))


burger = min(menu[:3])
drink = min(menu[3:])

print(burger + drink - 50)






# 저항(중급)
# color = {"black", "brown", "red", "orange",
#             "yellow", "green", "blue", "violet", "grey", "white"}

color = ["black", "brown", "red", "orange",
            "yellow", "green", "blue", "violet", "grey", "white"]
mul = [1, 10, 100, 1000,
       10000, 100000, 1000000, 10000000, 100000000, 1000000000]
select = (input("컬러 입력 3가지 : "))
f_name = color.index(input())
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name))




# PC방 알바(중급)







