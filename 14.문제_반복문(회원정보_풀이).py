# 회원 정보 출력하기 (1단계 → 현재 상태대로) (2단계 → 함수형태로 변환)

# 클래스로 객체 만들면 값을 가질수 있느냐 없느냐의 차이
# 함수형의 큰 특징 5개 중 상태를 가지면 안되는 특성.. → 객체를 만들지 말라는 뜻 // 객체는 필드가 가지는것임.

name = input("이름 : ")
while True:
    age = input("나이 : ")
    if age.isdigit():        # 입력받은 문자열이 숫자로 구성되어 있는지 확인 → 예외체크
        age = int(age)
        if 0 < age < 200 : break
    print("나이 잘못 쓰셨어영")

while True:
    gender = input("성별 : ")
    if gender == 'M' or gender == 'm' or gender == 'F' or gender =='f' : break
    print("성별 이상해영")

while True:
    jobs = input("직업 : ")
    if jobs.isdigit():          # 예외체크
        jobs = int(jobs)        # 형변환
        if 0 < jobs < 5 : break
    print("직업 잘 못 쓰셨어영")

if gender == 'M' or gender == 'm' : gen_str = "남성"
else: gen_str = "여성"

# 튜플()로 만드는 이유 : 바뀌는 내용이 아니라는것을 명시하기 위함. ()없이 사용가능.
# 튜플() : 이미 만들어진 데이터를 한 공간에 모아서 넣어놓은 것
jobs_str = ("", "학생", "회사원", "주부", "무직")

print("="*3, "회원정보", "="*3)
print(f"""이름 : {name}
나이 : {age}
성별 : {gen_str}
직업 : {jobs_str[jobs]}
""")


















