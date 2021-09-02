# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:


def Mountain(list_number):
    length =  len(list_number)
    if length < 3:
        return False
    else:
        i =0
        while i < length - 1:
            # print(list_number[i])
            if list_number[i] < list_number[i + 1]:
                i += 1
            else:
                break
        if i == 0 or i == length - 1:
            return False
        while i < length - 1:
            print(list_number[i])
            if list_number[i] > list_number[i + 1]:
                i += 1
            else:
                break
        if i == length - 1:
            return True
        else:
            return False

if __name__ == '__main__':
    arr = [0, 2, 3, 4, 5, 2, 1, 0]
    Mountain(arr)