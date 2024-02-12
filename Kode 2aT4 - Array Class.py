# Array5 - Ordered Array (with Class)
from Array2a import Array

maxSize = 10                      # Max size of the objArray
nItems = 0                        # No items in array initially

# driver
arr = Array(maxSize)           

arr.insert(9); arr.insert(3); arr.insert(11); arr.insert(7)
arr.traverse()
arr.insert(5)
arr.traverse()
arr.insert(1)
arr.traverse()
arr.insert(13)
arr.traverse()

target = 7
item = arr.search(target)
if item is None:
  print(f"{target} is not found!\n")
else:
  print(f"Found item : {item}\n")

target = 15
if arr.delete(target):
  print(f"Item {target} has been deleted!\n")
else:
  print(f"{target} is not found!\n")

# print(f"Array capacity : {maxSize}\n")
# print(f"Array size : {nItems}\n")