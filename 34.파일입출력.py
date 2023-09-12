# 파일쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야 함
# 파일삭제 : open(파일명, 파일모드, 인코딩)
# 파일명 : 파일 경로 + 파일명 (파일경로를 입력하지 않으면 현재 위치에 저장)
# 파일모드 : r(read) w(write) a(append 추가할 파일이 없으면, 만들어서 추가해줌, 있으면 파일의 마지막으로 추가)

score_file = open("score.txt", "w", encoding="utf-8")     # 여기서 "w"는 파일 모드.
print("수학 : 50", file=score_file)   # score_file에 대입시키는 개념
print("영어 : 98", file=score_file)
score_file.write("국어 : 98" + "\n")  # print는 기본적으로 마지막에 enter가 있지만, write는 따로 개행문자를 넣어줘야 줄바꿈을 함.
score_file.write("과학 : 45" + "\n")
score_file.close()


# 파일읽기
# read() : 파일내의 모든 내용을 읽어서 하나의 문자열로 반환함
# readline() : 해당 파일의 내용을 한 라인씩 읽어들여 문자열로 반환. 더이상 읽을 내용이 없으면 None반환
# readlines() : 해당 파일의 모든 라인을 순서대로 읽어, 각각의 라인을 하나의 요소로 저장하는 리스트로 반환

# score_file = open("score.txt", "r", encoding="utf-8")

# print(score_file.read())
# score_file.close()
# while True:
#     line = score_file.readline()        # 한줄 씩 읽음
#     if not line: break                  # 더 이상 읽을 라인이 없으면 None 값으로 확인되고, None은 거짓임.
#     print(line, end="")                 # 한줄 씩 읽어서 출력하기 때문에 줄바꿈 문자가 포함되어 있음
# score_file.close()

# lines = score_file.readlines()            # 해당 파일의 모든 라인을 순서대로 읽어서 리스트 생성
# for e in lines:
#     print(e, end="")
# score_file.close()

# with 키워드 사용하기 : open() 이후에 자동으로 close를 호출해주는 기능, 코드가 길어지면 close를 빠트리기 쉬움.
with open("score.txt", "r", encoding="utf-8") as score_file:
    print(score_file.read())            # 읽어라
    # 블럭에서 빠져나올때 (현재 이자리쯤)에서 close가 작동함
print("프로그램의 끝")

















