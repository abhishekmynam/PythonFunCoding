arr1 = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr2 = [int(arr_temp) for arr_temp in input().strip().split(' ')]
q = []
for a in range(arr1[2]):
    q.append(int(input().strip()))
l1 = arr1[-1:] + arr1[:-1]
l2 = l1[-1:] + l1[:-1]

for i in q:
    print(l2[i])
