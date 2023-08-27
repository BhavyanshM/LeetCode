

# n = 30
# [1, 10, 11, 12, 13, 14, 15,16,17,18,19,2,20,21,22]


def next_num(n, nums, mx):

    if int(n) <= mx:
        nums.append(n)

        for i in range(10):
            next_num(n+str(i), nums, mx)
    


if __name__ == "__main__":
    n = int(input().split(' ')[2])

    nums = []

    for i in range(1, 10):
        next_num(str(i), nums, n)

    print(nums)

