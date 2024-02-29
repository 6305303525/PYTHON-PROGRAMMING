from itertools import permutations

def unique_permutations(num):
    num_str = str(num)
    unique_perms = set(permutations(num_str))
    for perm in unique_perms:
        print(''.join(perm))

# Sample Input
num = 143
print(f"Given Number: {num}")
print("Permutations are:")
unique_permutations(num)
