# Given an array nums of integers, return how many of them contain an even number of digits.

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

def contain_digits(list_number):
    count = 0
    for number in list_number:
        digits = len(str(number))
        if (digits % 2) == 0:
            count+=1
    print(count)
    return count

if __name__ == '__main__':
    # [12, 345, 2, 6, 7896]
    list_number = [12, 345, 2, 6, 7896]
    contain_digits(list_number)