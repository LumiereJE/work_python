# 함수버전

def input_age():           # 함수이기 때문에 반환타입 없어도 됨
    while True:
        age = input("나이 : ")
        if age.isdigit():  # 입력받은 문자열이 숫자로 구성되어 있는지 확인 → 예외체크
            age = int(age)
            if 0 < age < 200: return age        # 반환
        print("나이 잘못 쓰셨어영")

def input_gender():
    while True:
        gender = input("성별 : ")
        if gender == 'M' or gender == 'm' : return "남성"
        elif gender == 'F' or gender == 'f': return "여성"
        else: print("성별 이상해영")

def input_jobs():
    while True:
        jobs = input("직업 : ")
        if jobs.isdigit():  # 예외체크
            jobs = int(jobs)  # 형변환
            if 0 < jobs < 5: return jobs
        print("직업 잘 못 쓰셨어영")

def print_info(name, age, gender, jobs):
    jobs_str = ("", "학생", "회사원", "주부", "무직")
    print("=" * 3, "회원정보", "=" * 3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"


member_info = "member.txt"                          # 입력받은 정보를 txt로 저장
fd = open(member_info, "wt", encoding="utf-8")      # "wt" w → 새로쓰는용도, t → 텍스트 모드      한글 깨져서 해준거임

# 함수는 선언 이후 호출해야 동작 함.
while True:
    name = input("이름 (종료 → quit 입력) : ")
    if name == 'quit' : break

    age = input_age()
    gender = input_gender()
    jobs = input_jobs()

    rst = print_info(name, age, gender, jobs)
    fd.write(rst + "\n")
fd.close()                                          # open( ) 썼으면 닫아줘야 함






















