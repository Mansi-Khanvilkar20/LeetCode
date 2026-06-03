class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) >= 2:
            total=0
            for i in str(num):
                total += int(i)
                num = total
        return num
