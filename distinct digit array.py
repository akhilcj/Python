nums = [12,9,67,8,9,12,10]
n = len(nums)
def distdigits(nums,n):
    for i in range(0, n):
        d = 0
        for j in range(0, i):
            if nums[i] == nums[j]:
                d = 1
                break

        if (d == 0):
            print(nums[i],end= ' ')

distdigits(nums,n)


