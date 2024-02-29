def productExceptSelf(nums):
    n = len(nums)
    prefix_products = [1] * n
    suffix_products = [1] * n
    for i in range(1, n):
        prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
    answer = [0] * n
    for i in range(n):
        answer[i] = prefix_products[i] * suffix_products[i]
    return answer
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
