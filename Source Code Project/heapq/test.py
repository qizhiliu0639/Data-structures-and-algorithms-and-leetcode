# import multiprocessing
# import time
#
# # First thread. We pass in one parameter
# def process1(param,Q1,Q2):
#     while True:
#         if not Q1.empty():
#             result = Q1.get()
#             result += 1
#             Q2.put(result)
#             print("This is process 1. x is %d" % result)
#             time.sleep(param)
#
#
# # Second process. We pass in two parameters
# def process2(param1, param2,Q1,Q2):
#     while True:
#         if not Q2.empty():
#             result = Q2.get()
#             result *= 2
#             Q1.put(result)
#             print("This is process 2. Param 2 is %d. x is %d" % (param2, result))
#             time.sleep(param1)
#
#
# def main(Q1,Q2):
#     # Create the first thread
#     p1 = multiprocessing.Process(target=process1, args=[1, Q1,Q2])
#     p1.start()
#     p2 = multiprocessing.Process(target=process2, args=[2, 123,Q1,Q2])
#     p2.start()
#
#
# if __name__ == '__main__':
#     Q1 = multiprocessing.Queue(1)
#     Q2 = multiprocessing.Queue(1)
#     Q1.put(1)
#     main(Q1,Q2)






# import multiprocessing
# import time
#
# # First thread. We pass in one parameter
# def process1(param,Q1):
#     while True:
#         result = Q1.get()
#         result += 1
#         Q1.put(result)
#         print("This is process 1. x is %d" % result)
#         time.sleep(param)
#
#
# # Second process. We pass in two parameters
# def process2(param1, param2,Q1):
#     while True:
#         result = Q1.get()
#         result *= 2
#         Q1.put(result)
#         print("This is process 2. Param 2 is %d. x is %d" % (param2, result))
#         time.sleep(param1)
#
#
# def main(Q1):
#     # Create the first thread
#     p1 = multiprocessing.Process(target=process1, args=[1, Q1])
#     p1.start()
#     p2 = multiprocessing.Process(target=process2, args=[2, 123,Q1])
#     p2.start()
#
#
# if __name__ == '__main__':
#     Q1 = multiprocessing.Queue(1)
#     Q1.put(1)
#     main(Q1)


import multiprocessing
import time
Q1 = multiprocessing.Queue(1)
Q1.put(1)

# First thread. We pass in one parameter
def process1(param):
    global Q1
    while True:
        result = Q1.get()
        result += 1
        Q1.put(result)
        print("This is process 1. x is %d" % result)
        time.sleep(param)


# Second process. We pass in two parameters
def process2(param1, param2):
    global Q1
    while True:
        result = Q1.get()
        result *= 2
        Q1.put(result)
        print("This is process 2. Param 2 is %d. x is %d" % (param2, result))
        time.sleep(param1)


def main():
    # Create the first thread
    p1 = multiprocessing.Process(target=process1, args=[1,])
    p1.start()
    p2 = multiprocessing.Process(target=process2, args=[2, 123])
    p2.start()


if __name__ == '__main__':
    main()