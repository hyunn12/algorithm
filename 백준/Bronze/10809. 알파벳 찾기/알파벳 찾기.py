S = input()

alphabet_arr = [-1] * 26
a_ascii = ord('a')

for index, char in enumerate(S):
    char_index = ord(char) - a_ascii
    if alphabet_arr[char_index] == -1:
        alphabet_arr[char_index] = index

print(' '.join(map(str, alphabet_arr)))
