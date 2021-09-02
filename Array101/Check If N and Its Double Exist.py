# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
#
# More formally check if there exists two indices i and j such that :


# Hide Hint #1
# Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
# Hide Hint #2
# On each step of the loop check if we have seen the element 2 * arr[i] so far or arr[i] / 2 was seen if arr[i] % 2 == 0.


def DoubleExist(list_number):
    N = len(arr)
    for i in range(N):
        try:
            if arr.index(arr[i] * 2) != i:
                return True
        except:
            continue
    return False


if __name__ == '__main__':
    # arr = [10, 2, 5, 3]
    # arr = [7, 1, 14, 11]
    arr = [3,1,7,11]

    DoubleExist(arr)
