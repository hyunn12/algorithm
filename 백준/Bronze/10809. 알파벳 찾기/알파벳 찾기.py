"""
[ 알파벳 찾기 ]
1. 알파벳 기록할 배열 alphabet_arr 선언한다
2. 알파벳 a의 아스키코드를 구한다
3. enumerate 를 이용해 입력받은 문자열을 각 문자와 인덱스로 분리해 반복문을 실행한다
4. 해당 문자의 아스키코드에서 a의 아스키코드를 빼 해당 문자의 알파벳 순서를 구한다
5. 해당 알파벳이 없었을 경우에만 등장위치인 index로 배열값을 초기화한다
6. 알파벳 배열을 공백으로 join 해 출력한다 
"""
S = input()

alphabet_arr = [-1] * 26
a_ascii = ord('a')

for index, char in enumerate(S):
    char_index = ord(char) - a_ascii
    if alphabet_arr[char_index] == -1:
        alphabet_arr[char_index] = index

print(' '.join(map(str, alphabet_arr)))
