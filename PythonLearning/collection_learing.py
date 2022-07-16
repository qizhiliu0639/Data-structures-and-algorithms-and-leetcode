from collections import *
import os, argparse
def chainMap_1():
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    c = ChainMap(baseline, adjustments)
    print(c.maps)

def chainMap_2():


    defaults = {'color': 'red', 'user': 'guest'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

    combined = ChainMap(command_line_args, os.environ, defaults)
    print(combined['color'])
    print(combined['user'])

def chainMap_3():
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    c = ChainMap(baseline, adjustments)
    d = c.new_child({'a' : 'b'})
    e = c.new_child({'c' : 'd'})
    print(c)
    print(d)
    print(e)

def chainMap_4():
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    c = ChainMap(baseline, adjustments)
    d = c.new_child({'a' : 'b'})
    print(c.parents)
    print(d.parents)


def counter_1():
    c = Counter(cats=4, dogs=5)
    print(c["fly"])
    print(c)

def counter_2():
    c = Counter("Abc")
    print(c)

def counter_3():
    c = Counter(a=4, b=2, c=0, d=-2)
    print(sorted(c.elements()))

def dequeue_1():
    d = deque("abc")
    for i in d:
        print(i.upper())

if __name__ == "__main__":
    # print(chainMap_1())
    # chainMap_1()
    # chainMap_2()
    # chainMap_3()
    chainMap_4()
    # counter_1()
    # dequeue_1()
    # counter_2()