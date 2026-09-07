nums=[10,20,30,40,50]
k=int(input())
n=len(nums)
if k>n:
    k=k%n

first=(nums[-k:])
last=(nums[:-k])
first=first[::-1]
print(first+last)



