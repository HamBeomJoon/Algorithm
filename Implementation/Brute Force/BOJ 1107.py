# 백준 1107번: 리모컨 (Gold 5)
# 무지성 완전탐색.. 수를 100만까지 확인하는 이유는 7버튼만 사용할 수 있을 때
# 77777에서 50만을 가는것 보다 777777에서 50만을 가는것이 더 빠르기 때문

N = int(input())
M = int(input())
button = set(i for i in range(10))
remove_button = set(map(int,input().split()))
# button에서 사용할 수 없는 remove button을 제거해준다.
button -= remove_button
answer = abs(100 - N)

for i in range(1000001):
    tf = True
    for j in range(len(str(i))):
        # 1부터 100만까지 확인해가며 각 자리수를 반복문을 돌며 사용할 수 있는 버튼인지
        # 확인해준다. 사용못하는 버튼이면 tf = False로 바꿔준 뒤 break
        if int(str(i)[j]) not in button:
            tf = False
            break
    
    # tf가 True이면 answer값 갱신 -> 
    # 현재 숫자 누르는 횟수 len(str(i)) + 그 숫자에서 N까지의 차이 abs(i - N)
    if tf:
        answer = min(answer, len(str(i)) + abs(i - N))
print(answer)
