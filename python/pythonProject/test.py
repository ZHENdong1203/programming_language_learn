from itertools import combinations
length = int(input())
str_list = input().split()
number_index = int(input())

comb = list(combinations(str_list,number_index))

count = 0
for c in comb:
    if 'a' in c:
        count += 1

comb_length = len(comb) if len(comb) > 0 else 1
result = count / comb_length
print(f"{result:.4f}")
