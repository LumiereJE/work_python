# 튜플 : 변경할 수 없는 시퀀스 자료형 (나머지는 리스트와 동일)
# 튜플의 정의 : ()괄호를 사용 or 생략 가능

# 튜플 만들기
person = "곰돌이사육사", 20, "서울시 강남구 역삼동"      # 괄호가 없으면 (,)로 구분함. 붙이면 튜플임.
print(person)

# 튜플 요소로 접근하기
# print(person[0])
# print(person[1])

# 튜플의 언패킹
# 이름, 나이, 주소 = person
# print(이름)
# print(나이)
# print(주소)

# 튜플의 언패킹 기능을 이용한 함수 만들기
def get_person() :
    name = "가을"
    age = 23
    addr = "서울시 강남구 역삼동"
    return name, age, addr;

result = get_person();      # 언패킹되어서 전달되는 반환값을 패킹해서 받음
print(result)

a, b, c = get_person()
print(a)
print(b)
print(c)


tp = 1,1,2,2,2,3,3,3,3
print(tp.count(3))      # 매개변수로 전달한 변수가 몇 번 등장하는지 확인하는 함수
print(tp.index(2))      # 매개변수로 전달한 변수의 시작 인덱스를 반환
print(len(tp))

# 튜플에서 안되는 것 (immutable특성이 있기 때문에 삭제할 수 없음)
del tp[0]


# 패킹
tuple1 = 10, "열", True

# 언패킹
a, b, c = tuple
print(a)
print(b)
print(c)
















