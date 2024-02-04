arr = [4,2,3,4,5]
min = arr[0]
for i in range (len(arr)):
   if  min > arr[i]:
    min = arr[i]

print(min)