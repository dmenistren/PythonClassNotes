def comp(array1, array2): 
    # 1. Handle None cases
    if array1 is None or array2 is None:
        return False
    
    # 2. If lengths are different, they can't be "the same"
    if len(array1) != len(array2):
        return False

    # 3. Square all elements in array1 and sort both
    # We take the absolute value of array1 elements because (-n)^2 == n^2
    squared_a1 = sorted([x * x for x in array1])
    sorted_a2 = sorted(array2)

    # 4. Compare the sorted lists
    return squared_a1 == sorted_a2

# Test Cases
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))          # Output: True
print(comp([1,2,3], [1,4,9])) # Output: True
print(comp([1,2], [1,4,9]))   # Output: False