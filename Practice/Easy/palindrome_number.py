
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        if x == 0:
            return True

        palin = True

        num_len = int(math.log10(x))

        for i in range(num_len + 1):
            ds = get_digit(i, x)
            de = get_digit(num_len - i, x)

            if ds != de:
                palin = False

        return palin
    
def get_digit(i, x):

    return int((x % math.pow(10, i+1)) // math.pow(10, i))


if __name__ == "__main__":

    solution = Solution()

    num = -0
    
    result = solution.isPalindrome(num)

    if result:
        print("true")
    else:
        print("false")

    