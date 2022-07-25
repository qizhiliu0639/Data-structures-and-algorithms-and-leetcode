# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from sortedcontainers import SortedList

def test():

    a = SortedList()
    a.add([16, "sushi"])
    a.add([16, "ramen"])
    a.add([15, "gg"])
    print(a)

def NumberOf1(n):
    return bin(n & 0xffffffff).count('1')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(NumberOf1(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
