"""
[ 배열 내 가장 큰 수 찾기 ]
1. 입력받은 배열을 반복문을 통해 요소를 탐색한다.
2. 해당 숫자가 max_num 보다 클 경우 max_num 를 해당 숫자로 대체한다.
3. 최종 max_num 을 반환한다.
"""

max_num = 0
index = 0

for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        index = i + 1

print(max_num)
print(index)
