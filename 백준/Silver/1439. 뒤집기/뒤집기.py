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
