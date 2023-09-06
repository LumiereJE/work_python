# 각 사이트 비밀번호 만들기
# 규칙1 : http://naver.com 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점 이후 제거
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o'갯수 + 글자에 포함된 'k'의 갯수 + "!" + 자신의 이니셜

file_name = "password.txt"
fd = open(file_name, "wt")      # txt모드 기본값.

while True:
    url = input("사이트 : ")
    if url == 'exit': break

    my_str = url.replace("http://", "")     # http 지우기
    my_str = my_str[:my_str.index(".")]                 # 슬라이싱 : 처음부터 "."인덱스 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k"))+ "!" + "jks"   # 앞에서부터 3개(nav) 자르기
    print("비밀번호 : " + password)     # 비밀번호 찍어줌

    fd.write(password + "\n")   # 파일 만들어 줌

fd.close()  # while문 빠져 나오면 닫도록.







