# import math         # math 모듈을 사용하기 위해서 import 함
# print(math.sin(1))
# import math
# # 모듈 내에 함수(메서드) 특정한 함수만 가져오고자 하는 경우
# from math import sin, cos, tan
# print(sin(1))               # math안에 있는 함수만 가져와 짐
# print(cos(1))
# print(tan(1))

# 모듈을 가져올때 충돌이나 긴 이름을 간결하게 하용하기 위해서 별칭을 부여함 (별칭을 부여하면 원래이름 사용 불가)
# import math as m
# print(m.sin(1))
#
# # sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# import sys
# print("명령 줄 인수 : ", sys.argv)
# print("실행 경로 : ", sys.path[0])
# sys.stdout.write("Hello, world !!! \n")         # std = standard
# sys.stdout.write("Error !!! \n")
# sys.exit(0)                                     # 강제 종료 (운영체제가 직접 죽이는것)

# os 모듈 : 운영체제와 상호 작용하기 위한 기능을 제공함 (파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등)
import os
cwd = os.getcwd()                     # cwd : 현재 작업 디렉토리
print("현재 작업 디렉토리 : ", cwd)
# 디렉토리 생성
# os.mkdir("testDir")                 # 디렉토리 폴더 생성, 이미 만들어진 상태에서 또 돌리면 오류남
is_dir = os.path.isdir("testDir")
if not is_dir: os.mkdir("testDir")    # 폴더 없으면 생성해라
is_file = os.path.isfile("score.txt")
print(is_file)

os.system("dir")



