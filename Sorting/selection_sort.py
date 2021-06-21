# Selection Sort implemented in Python 3
# 
# Time complexity: 
# Space complexity:
# 
# Input: Unsorted array
# Output: Sorted array


# Utility function getSmallest
# Returns the index of the smallest element in the array
# Input: array
# Output: index of the smallest element
def getSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]        # new smallest integer
            smallest_index = i         # index of smallest integer
    return smallest_index


def selection_sort(array):
    newArray = []                       # temporary array to hold the sorted array
    for i in range(len(array)):
        smallest = getSmallest(array)      # get the index of the smallest element
        newArray.append(array.pop(smallest))       # add the element to the end of the array
    return newArray

if __name__ == "__main__":
    array = [6,1,3,10,2,31]
    print (selection_sort(array))
