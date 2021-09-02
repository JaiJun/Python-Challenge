# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.

def Duplicate(list_number):
    i = 0
    while i < len(list_number):
        if list_number[i] != 0:
            i+=1
        else:
            list_number.insert(i+1, 0)
            i+=2
            list_number.pop()
    return list_number
if __name__ == '__main__':
    list_number = [1,2,3,4,5,0]

    print(Duplicate(list_number))
