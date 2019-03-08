def quick_sort(li,first,last):
    start = first
    end = last
    if start < end:
        mid = li[first]
        while start < end:
            print(start,end,"循环内")
            while start < end and li[end] >= mid:
                end -= 1
            li[start],li[end] = li[end],li[start]
            print(li, 222)
            while start < end and li[start] <= mid:
                start += 1
            li[start], li[end] = li[end], li[start]
            print(li, "经历一次排序", mid)
        print(0,start-1,"排的是左边从{}到{}".format(0,start-1))
        quick_sort(li,0,start-1)
        print(100*"*")
        print(start+1,last,"排的是右边从{}到{}".format(start+1,last))
        quick_sort(li,start+1,last)
    else:
        print("单")
if __name__ == '__main__':
    li = [9, 3, 10, 8, 5, 7, 1, 9]
    last = len(li)-1
    quick_sort(li,0,last)



