# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.

def replaceElements(arr):
    last_num = -1
    # for i in range(len(arr)):
    #     try:
    #         arr[i] = max(arr[i + 1:])
    #     except:
    #         arr[i] = last_num
    for i in range(len(arr) -1, -1 , -1):
        newMax = max(last_num, arr[i])
        arr[i] = last_num
        last_num = newMax
    return arr






if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    replaceElements(arr)