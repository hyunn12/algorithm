"""
[ 뒤집기 ]
1. 전체를 0 으로 바꾸는 횟수와 1 로 바꾸는 횟수를 기록할 변수를 선언한다
2. 만약 입력받은 문자열이 0으로 시작한다면 1로 바꾸는 횟수에 1을 더하고, 
    1로 시작한다면 0으로 바꾸는 횟수에 1을 더한다
3. 문자열을 반복하면서 해당 문자가 다음 문자와 다르다면, 같게 하기위해 뒤집어야한다는 뜻이므로
    다음 문자가 0으로 시작한다면 1로 바꾸는 횟수에 1을 더하고,
    1로 시작한다면 0으로 바꾸는 횟수에 1을 더한다
4. 0으로 바꾸는 횟수와 1로 바꾸는 횟수 중 작은 수를 반환한다
"""

string = input()

count_to_zero = 0
count_to_one = 0

if string[0] == '0':
    count_to_one += 1
else:
    count_to_zero += 1

for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        if string[i + 1] == '0':
            count_to_one += 1
        else:
            count_to_zero += 1
print(min(count_to_zero, count_to_one))
