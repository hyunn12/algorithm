"""
[ 최빈값 구하기 ]
1. 주어진 배열의 각 숫자를 세기 위해 count_arr 선언한다
2. 배열을 순회하면서 각 숫자의 빈도를 센다
3. 가장 많이 나온 횟수를 max_count 로 저장한다
4. max_count와 갯수가 같은 요소를 occurred_arr 에 저장한다
5. 만약 최빈값이 2개 이상인 경우 -1 을 반환한다
6. 아닌 경우 해당 값을 반환한다
"""

def solution(array):

    count_arr = {}

    for num in array:
        if num in count_arr:
            count_arr[num] += 1
        else:
            count_arr[num] = 1

    max_count = max(count_arr.values())
    occurred_arr = []
    for num, count in count_arr.items():
        if count == max_count:
            occurred_arr.append(num)

    if len(occurred_arr) > 1:
        return -1
    return occurred_arr[0]
