"""
Day 48: Binary Search
Write a function called search_binary that searches for the number 22 in the following
list and returns its index. The function should take two parameters, the list and 
the item that is being searched for. Use binary search (iterative Method).
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
"""
def search_binary_one(items:list, item_to_serch):
    #get sorted list
    items = sorted(items)
    low = 0
    high = len(items)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2 #get middle index.
        if items[mid] < item_to_serch:
            low = mid + 1
        elif items[mid] > item_to_serch:
            high = mid - 1
        else:
            return mid
    return -1


# test
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
print(search_binary_one(list1, 13))
