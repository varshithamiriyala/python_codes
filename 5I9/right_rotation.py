nums=[30,40,70,80,60]
k=int(input())
n=len(nums)
if k>n:
    k=k%n

first=(nums[k:])
last=(nums[:k])
print(first+last)

