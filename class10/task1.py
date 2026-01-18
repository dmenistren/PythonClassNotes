def comp(array1: list, array2: list) -> bool:
    # 1. Handle None cases
    if array1 is None or array2 is None:
        return False
    
    # 2. If lengths are different, they can't be "the same"
    if len(array1) != len(array2):
        return False

    # 3. Square all elements in array1 and sort both
    # We take the absolute value of array1 elements because (-n)^2 == n^2
    squared_a1 = sorted([x ** 2 for x in array1])
    sorted_a2 = sorted(array2)

    squared_b1 = sorted([x * x for x in array2])
    sorted_b2 = sorted(array1)

    # 4. Compare the sorted lists
    return squared_a1 == sorted_a2 or squared_b1 == sorted_b2


if __name__ == "__main__":
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(b, a))
    # print(comp([1,2,3], [1,4,9]))
    # print(comp([1,2], [1,4,9]))
