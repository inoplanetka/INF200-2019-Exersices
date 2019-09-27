def bubble_sort(input_data):
    nums = len(input_data)
    list_sorted = list(input_data)
    for x in range(nums):
        for z in range(0, nums - x - 1):
            if list_sorted[z] > list_sorted[z + 1]:
                list_sorted[z], list_sorted[z + 1] = list_sorted[z + 1], list_sorted[z]
    return list_sorted


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
