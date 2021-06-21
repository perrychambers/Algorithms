# Binary Search implemented in Python 3
# Time Complexity: O(log n)
# Space Complexity: O(n)
#
# Input: Sorted List, Key
# Output: Index of the key or None if does not exist

def binary_search(list, item):
    low = 0     
    high = len(list) - 1   

    while low <= high:          # while list not narrowed down to 1 element
        mid = (low + high) // 2  # get the middle element   // indicates floor division
        guess = list[mid]       
        if guess == item:       # item found
            return mid         
        if guess > item:        # guess was too high
            high = mid - 1
        else:                   # guess was too low
            low = mid + 1
    return None                 # not found

if __name__ == "__main__":
    list = [1,3,5,7,9]
    #unsorted_list = [6,1,3,10,2,31]
    #sorted_list = selection_sort(unsorted_list)

    print (binary_search(list, 3))
    #print (binary_search(3, sorted_list))

