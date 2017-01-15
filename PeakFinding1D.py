import sys
import math

def FindPeak(arr,Arr):
    n1 = math.floor((len(arr))/2)
    arr1 =arr[:n1]
    arr2 = arr[n1:]
    if(n1-1>=0 and n1+1<len(arr)):
        if(arr[n1-1]<= arr[n1] and arr[n1+1]<=arr[n1]):
            return arr[n1]
        else:
            value = FindPeak(arr1,arr)
            if(value is None):
                value = FindPeak(arr2,arr)
            return value
    else:
        if(arr[n1]>=Arr[n1+1]):
            return arr[n1]

n = int(input().strip())
Arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
peak= FindPeak(Arr,Arr)
print(peak)