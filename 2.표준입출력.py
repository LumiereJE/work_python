print(38)               # 정수형
print("문자열")          # 문자열
print([1, 2, 3])        # 리스트형
print(1+3)

print("파"+"이"+"썬")    # 문자열 이어붙이기
print("파""이""썬")
print("파","이","썬")    # ,(콤마)를 구분자라고 부름 → 한칸의 공백을 가지고 있음
print("파\n\n\n이\t\t썬") # escape문자

print("안녕하세요라고 \"곰돌이사육사\"가 말했습니다.")

# end와 sep옵션
# end : 출력부분에서 끝에 자동으로 삽입되는 문자를 지정하는 옵션 : \n
# sep : 출력문의 중간에 삽입되는 문자를 지정하는 옵션 : 기본은 space

print("Hello", end = "\n")
print("Hello", end = "$")
print("Hello", end = "*")
print("Hello")

print("lice", "is", "too", "short", sep="\\")
print("101","1234", "4578", sep="=")

year = 2023
month = 9
day = 6
print(year, month, day, sep="/")


