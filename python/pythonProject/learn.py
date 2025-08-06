from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    order_set = OrderedDict()
    number = len(string) // k
    listStr = list(string)
    for i in range(number):
        for j in listStr[i*k:(i+1)*k]:
            order_set[j] = 1
        print("".join(order_set.keys()))
        order_set.clear()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)