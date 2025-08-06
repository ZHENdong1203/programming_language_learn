# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
listA = set(map(int, input().split()))
listB = set(map(int, input().split()))

interA = listA.intersection(array)
interB = listB.intersection(array)
happy = 0
for i in interA:
    happy += array.count(i)
upset = 0
for j in interB:
    upset += array.count(j)
happiness= happy - upset

print(happiness)