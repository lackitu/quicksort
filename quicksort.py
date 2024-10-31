def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[j], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

inp1 = input("Give me some random numbers: \n")
inp1split = inp1.split()
data = [int(num) for num in inp1split]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order: ')
print(data)

#Quicksort is a popular sorting algorithm that uses a divide-and-conquer strategy to effciently sort elements. 
#It works by selecting a "pivot" element from the aray, 
#Partitioning the other elements into two sub-arrays based on whether they are less than or greater than the pivor, and then recursively sorting the sub-arrays. 
#Its average time complexity is O(n log n), making it faster than manu other sorting algorithms for large datasets.
#This is a simple example of course but can be used in bigger projects
#            +-------------------+
#            |    QuickSort      |
#            +-------------------+
#                      |
#           +----------+----------+
#           |                     |
#        Choose Pivot        Partition
#           |                     |
#     +-----+-----+         +----+----+
#     |           |         |         |
#    <Pivot     >Pivot    <Sub1>   <Sub2>
#    /           \         /         \
#   /             \       /           \
# Recursively   Recursively   Sort     Sort
#   Sort          Sort       Sub1      Sub2
#
