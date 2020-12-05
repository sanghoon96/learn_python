# os.mkdir("newdir") : Directory 생성
import os
os.mkdir("./dir01")
# ➢ os.getcwd() : 현재 위치
# ➢ os.chdir(directory) : 디렉토리 이동.
os.chdir(os.getcwd()+'/dir01')
print(os.getcwd())
# ➢ os.rmdir('dirname') : Directory 삭제
os.mkdir("./dir01")
# os.rmdir("./dir02")

# os.path.exists(file_name) : file 또는 Directory 유무
print(os.path.exists('./test/hellow.py'))
# ➢ os.remove(file_name) : 파일 삭제
# os.remove(‘hellow.py’)