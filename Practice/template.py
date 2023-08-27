class Solution:
    def functionName(self, moves: str) -> int:
        
        L_str = moves.replace("_", "R")
        R_str = moves.replace("_", "L")

        count_one = compute_final_position(L_str)
        count_two = compute_final_position(R_str)

        max_count = max(abs(count_one), abs(count_two))

        return max_count

def compute_final_position(moves):

    count = 0
    for m in moves:
            if m == "R":
                count+=1
            elif m == "L":
                count-=1

    return count


if __name__ == "__main__":

    solution = Solution()

    moves = "L_RL__R"
    
    count = solution.functionName(moves)

    

        