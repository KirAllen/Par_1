arr = [-1,-2,-3,-6,0,0,0,4,5,6,8,20,303030]

def sort_imperative(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr

print(sort_imperative(arr))

print()

def sort_declarative(arr):
    arr.sort(reverse=True)
    return arr

print(sort_declarative(arr))