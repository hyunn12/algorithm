"""
[ 소수 구하기 ]
1. 소수 여부 판별할 is_prime 선언한다
2. 1은 소수가 아니므로 무시한다
3. 반복문 내에서 해당 요소의 제곱근까지 다시 반복하면서 나눠지는 수가 있는지 확인한다 >> 소수 판별 식인 '에라토스테네스의 체' 사용
4. 나누어 떨어지는 수가 없다면 소수이다
"""
m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
