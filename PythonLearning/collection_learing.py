from collections import *
import os, argparse
def chainMap_1():
    baseline = {'music': 'bach', 'art': 'rembrandt'}
    adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    return list(ChainMap(adjustments, baseline))

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


if __name__ == "__main__":
    # print(chainMap_1())
    chainMap_2()