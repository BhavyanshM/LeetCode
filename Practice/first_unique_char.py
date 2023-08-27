class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        alpha = [[-1, 0] for i in range(26)]

        for i,c in enumerate(s):
            if alpha[ord(c) - ord('a')][0] == -1: # never seen before
                alpha[ord(c) - ord('a')][0] = i
            
            alpha[ord(c) - ord('a')][1] += 1

        ans = -1
        for i,c in enumerate(s):
            first_index = alpha[ord(c) - ord('a')][0]
            count = alpha[ord(c) - ord('a')][1]

            if first_index != -1 and count == 1: # never seen before
                ans = i
                break
            
        return ans




if __name__ == "__main__":
    s = Solution()

    index = s.firstUniqChar("aabb")

    print(index)

# AA00BXO5WD

# SEVIS ID: N0013624018