# Find the missing Number From the Given List
# i/p : list1 = [1,2,3,4,6,7,8,9]
#o/p : 5 is missing Number


def find_missing_element(nums):
    n = len(nums) + 1
    total_sum = n*(n+1)//2
    actual_sum = sum(nums)

    return total_sum - actual_sum


nums = [1,2,3,4,6,7,8,9]
missing_elements = find_missing_element(nums)
print(f"{missing_elements} is the missing elements")


