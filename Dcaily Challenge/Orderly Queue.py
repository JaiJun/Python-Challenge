"""
    You are given a string s and an integer k.
    You can choose one of the first k letters of s and append it at the end of the string..

    Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.
"""


def orderlyQueue(s, k):
    # if k == 1:
    #     N = len(s)
    #     best = s
    #     for start in range(N):
    #         current = s[start:] + s[:start]
    #         if current < best:
    #             best = current
    #     return best
    # return "".join(sorted(s))
    if k > 1: return ''.join(sorted(s))
    ans = s
    for i in range(0, len(s)):
        ans = min(ans, s[i:] + s[0:i])
    return ans

if __name__ == '__main__':
    s = "cba"
    k = 1
    result = orderlyQueue(s, k)
    print(result)