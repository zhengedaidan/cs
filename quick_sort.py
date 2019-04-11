def quick_sort(l,start,end):
    left = start
    right = end
    if left< right:
        key = l[start]
        while left < right:
            while left < right and l[right] >= key:
                right -= 1
            l[left],l[right]= l[right],l[left]
            while left<right and l[left] <= key:
                left +=1
            l[left], l[right] = l[right], l[left]
        quick_sort(l,0,left-1)
        quick_sort(l,left+1,end)
if __name__ == '__main__':
    l = [1,2,4,2,3,9,8,7]
    start = 0
    end = len(l)-1

    quick_sort(l,start,end)

    print(l)

