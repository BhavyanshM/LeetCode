class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        
        
        min_sum = compute_minimum_sum(n, 0, target, )

        return max_count

def compute_minimum_sum(n, n_level, target, sum_so_far, num_so_far, barray, dp):

    if n == 1:
        return 1

    if n_level == n:
        return sum_so_far

    valid = True

    new_num = num_so_far + 1

    for i in barray:
        if i + new_num == target:
            valid = False

    if valid:
        barray.append[new_num]
        dp[n_level] = min(dp[n_level], compute_minimum_sum(n, n_level+1, target, sum_so_far + new_num, barray, dp)


    return count


if __name__ == "__main__":

    solution = Solution()

    moves = "L_RL__R"
    
    count = solution.functionName(moves)

    

        
# n = 5, target = 15
# [1,2,3,4,5]
