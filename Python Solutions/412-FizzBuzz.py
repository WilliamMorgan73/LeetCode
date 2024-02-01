class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range (1, n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


'''
Original solution\

        ans = [0] * n
        for i in range (0, n):
            j = i+1
            if j % 15 == 0:
                ans[i] = "FizzBuzz"
            elif j % 3 == 0:
                ans[i] = "Fizz"
            elif j % 5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(j)
        return ans


'''
