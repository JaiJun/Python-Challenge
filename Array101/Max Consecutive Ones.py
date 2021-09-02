# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

def maximum_consecutive(list_number):
    count = 0
    history_count = []
    for number in list_number:
        if number == 1:
            count+=1
        else:
            count = 0
        history_count.append(count)
    return max(history_count)

if __name__ == '__main__':
    # [1, 0, 1, 1, 0, 1]
    list_number = [1,1,0,1,1,1]
    maximum_consecutive(list_number)