# Bubble Sort
#
# Input: array
# Output: sorted array by ascending

def bubble_sort(array):
    length = len(array)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                swapped  = True
                array[j], array[j+1] = array[j+1], array[j]     # do the swapping
        if not swapped:
            break
    return array

if __name__ == "__main__":
    user_input = input("Enter numbers to be added to array separated by comma:").strip()
    # parse the user input in to an unsorted array
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"Unsorted array: {unsorted}")
    print(f"Sorted array: {bubble_sort(unsorted)}")
