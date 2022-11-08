"""
Description:
Author:qxy
Date: 2019-09-16 15:50
File: 00050_powx_n 
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        i = n
        if i < 0:
            i = -i
        res = 1
        while i != 0:
            if i % 2 != 0:
                res *= x
            x *= x
            i = i // 2
            print(i)
        return res if n > 0 else 1 / res


a = Solution()
da = a.myPow(2.000, 10)
print(da)