import time
from time import sleep

hour, minute, second = 0, 0, 0
y_n = " "
#타이머 지정 함수
def set_timer():
    global hour, minute, second, y_n
    print("숫자만 입력해주세요")
    time.sleep(1)
    hour = int(input("시간을 입력해 주세요\n"))
    minute = int(input("분을 입력해 주세요\n"))
    second = int(input("초를 입력해 주세요\n"))
    print(f"입력한 시간이{hour}시간 {minute}분 {second}초가 맞습니까?")
    y_n = input("(네/아니요)")
#함수 사용
set_timer()
#대답
if y_n == "아니요":
    set_timer()