"""
    說明:
    You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

     You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

     The first element in s[k] starts with the selection of the element nums[k] of index = k.
     The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
     We stop adding right before a duplicate element occurs in s[k].
     Return the longest length of a set s[k].
"""
from urllib3.connectionpool import xrange


def arrayNesting(nums):
     """
     Sample :
          初始:
          num[0] = 5 此index為0，值為5
          ----------------------------
          num[5] = 6 此index為5，值為6
          num[6] = 2 此index為6，值為2
          num[2] = 0 此index為2，值為4
          num[0] = 5 此index為2，值為4 ->> 回到起始點
     """
     if len(nums) == 0:
          return 0
     else:
          visited = [False] * len(nums)
          result = 0
          for i in xrange(len(nums)):
               road = 0
               # print(nums[i])
               while not visited[i]:
                    road += 1
                    visited[i] = True
                    i = nums[i]
               result = max(result, road)
          return result


if __name__ == '__main__':
     nums = [5, 4, 0, 3, 1, 6, 2]
     arrayNesting(nums)
