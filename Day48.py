"""
Day 48: Binary Search
Write a function called search_binary that searches for the number 22 in the following
list and returns its index. The function should take two parameters, the list and 
the item that is being searched for. Use binary search (iterative Method).
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
"""

def search_binary(items:list, item_item_serch):
    for i in range(len(items)):
        if items[i] == item_item_serch:
            return i
    return f'{item_item_serch} not found!!'