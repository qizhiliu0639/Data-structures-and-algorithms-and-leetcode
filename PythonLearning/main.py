# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def solution(S):
    # write your code in Python (Python 3.6)
    ans = float('inf')
    # if len(S) > 100000:
    #     return -1

    ind = []
    distance = []
    for i in range(len(S)):
        if S[i] == 'R':
            if ind:
                distance.append(i - ind[-1] - 1)
            ind.append(i)
    if not ind:
        return 0
    sumValue = sum(distance)
    if sumValue >= 10 ** 9:
        return -1
    front = [0]
    backend = [sumValue]
    for i in distance:
        front.append(i + front[-1])
        backend.append(backend[-1] - i)
    for i in range(len(front)):
        ans = min(front[i] + backend[i], ans)

    print(ans)
    print(front)

    if ans > 10 ** 9:
        return -1
    else:
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # d = {
    #     2: [0, 2, 3],
    #     4: [1],
    #     5:[0, 1, 4],
    #     6:[2]
    # }
    #
    # a = sorted(d.items(), key=lambda x: len(x[1]), reverse=False)
    # print(a)
    S = 'RW' * 100000
    print(solution(S))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
