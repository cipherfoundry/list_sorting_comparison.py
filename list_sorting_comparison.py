# This script demonstrates the difference between a sorted list 
# and the original unsorted data.
nums = [10, 3, 8, 1]
sorted_nums = [10, 3, 8, 1]

nums.sort()

print(nums)         # Shows the new order: [1, 3, 8, 10]
print(sorted_nums)  # Shows the original order: [10, 3, 8, 1]
print(nums == sorted_nums) # Returns False because the orders don't match
