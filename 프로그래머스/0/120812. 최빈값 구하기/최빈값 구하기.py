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