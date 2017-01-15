import sys
import math
import numpy

def column(matrix, i):
    return [row[i] for row in matrix]
def FindPeak2D(arr, Arr, n, m):
    m1 = math.floor(m/2)
    colList = column(arr,m1)
    maxVal = max(colList)
    num_rows, num_cols = arr.shape
    n1 = colList.index((maxVal))
    if(m1!=0 or m1+1<=num_cols):
        if(maxVal>= arr[n1,m1-1] and maxVal>= arr[n1,m1+1]):
            return maxVal
        else:
            if (maxVal < arr[n1, m1 - 1]):
                maxVals = FindPeak2D(arr,arr, num_rows,num_cols-m1)
                return maxVals
            elif (maxVal < arr[n1, m1 + 1]):
                maxVals = FindPeak2D(arr, arr, num_rows,num_cols-m1)
                return maxVals
    else:
        return  maxVal




i,j=5,5
arr = numpy.zeros((i,j))
for x in range(i):
    for y in range(j):
        arr[x,y]=int(input())
print(FindPeak2D(arr,arr, i,j))