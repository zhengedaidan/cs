def quick(li, start, end):
    if start >= end:
        return
    left = start
    right = end
    key = li[start]

    while left < right:
        while left < right and li[right] >= key:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= key:
            left += 1
        li[right] = li[left]
    li[left] = key
    quick(li, start, left - 1)
    quick(li, left + 1, end)

def binary(li, key):
    min = 0
    max = len(li)-1
    if key in li:
        while True:
            center = (min+max)//2
            if li[center]>key:
                max = center-1
            elif li[center] <key:
                min = center+1
            else:
                print("位置是{}值是{}".format(center,li[center]))
                return
    else:
        print("no")


if __name__ == '__main__':
    l = [5,6,9,7,3]
    s = 0
    e = len(l) - 1
    quick(l, s, e)
    print(l)
    binary(l,3)
