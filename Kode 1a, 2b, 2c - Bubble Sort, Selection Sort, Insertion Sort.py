import os; os.system("cls")
# number1 = [8, 9, 3, 10, 6, 0, 7, 4, 11, 2, 1, 5]
# number2 = [5, 2, 4, 3, 1]
# number3 = [8, 5, 7, 1, 9, 3]

list1 = [9, 1, 11, 7, 3, 13, 5]
list2 = [10, 4, 14, 8, 2, 12, 6]
list3 = ["John", "Jack", "Jane", "Jill"]
list4 = ["A", "a", "Z", "z", "1", "10"]

print(f"Unsorted list: {list4}")

""" Bubble Sort """
# def bubbleSort(list, asc):
#     for j in range(len(list)-1):
#         for i in range(len(list)-(j+1)):
#             if asc == "A":
#                 if list[i] > list[i+1]:
#                     list[i], list[i+1] = list[i+1], list[i]
#             elif asc == "D":
#                 if list[i] < list[i+1]:
#                     list[i], list[i+1] = list[i+1], list[i]
#             print(j, i, list)
# bubbleSort(list4, "A")

# def bubbleSortOpt(list, asc):
#     while True:
#         swapped = False
#         for j in range(len(list)-1):
#             if asc == "A":
#                 if list[j] > list[j+1]:
#                     list[j], list[j+1] = list[j+1], list[j]
#                     swapped = True
#             elif asc == "D":
#                 if list[j] < list[j+1]:
#                     list[j], list[j+1] = list[j+1], list[j]
#                     swapped = True
#             print(j, list)
#         if not swapped:
#             break
# bubbleSortOpt(list4, "A")

""" Selection Sort """
# def selectionSort(list, asc):
#     for j in range(len(list)-1):
#         index_i, small = 0, list[j]
#         for i in range(j+1, len(list)):
#             if asc == "A":
#                 if list[i] < small:
#                     index_i, small = i, list[i]
#             elif asc == "D":
#                 if list[i] > small:
#                     index_i, small = i, list[i]
#         if index_i != 0:
#             list[index_i], list[j] = list[j], list[index_i]
#         print(j, i, index_i, list)
# selectionSort(list4, "A")
    
""" Insertion Sort """
# def insertionSort(list, asc):
#     for j in range(1, len(list)):
#         num = list[j]
#         index = j-1
#         print(j, index)
#         if asc == "A":
#             while index >= 0 and num < list[index]:
#                 list[index+1] = list[index]
#                 print(index, index+1, list)
#                 index -= 1
#         if asc == "D":
#             while index >= 0 and num > list[index]:
#                 list[index+1] = list[index]
#                 print(index, index+1, list)
#                 index -= 1
#         list[index+1] = num
#         print(list, "\n")
# insertionSort(list4, "A")

# def insertionSort51(list, asc):
#     for j in range(1, len(list)):
#         num = list[j]
#         index = j
#         print(j, index)
#         if asc == "A":
#             while index > 0 and num < list[index-1]:
#                 list[index] = list[index-1]
#                 print(index, index+1, list)
#                 index -= 1
#         if asc == "D":
#             while index > 0 and num > list[index-1]:
#                 list[index] = list[index-1]
#                 print(index, index+1, list)
#                 index -= 1
#         list[index] = num
#         print(list, "\n")
# insertionSort51(list4, "A")

print(f"Sorted list: {list4}")