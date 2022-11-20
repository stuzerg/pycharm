import time
# digit_r = [11, 2, 9, 7, 155, 1, 3, 2]
# #digit_row.insert(6,33)
# print(digit_r)
#
#
#
# le_ = len(digit_r)
# print(le_)
# count_  = 0
#
# # int(len(digit_row)/2+1)
# for j in range(1, int(len(digit_r))):
#     for i in range (j, len(digit_r) - j + 1):
#         count_ += 1
#         if digit_r[i - 1] > digit_r[i]:
#             digit_r[i], digit_r[i - 1] = digit_r[i - 1], digit_r[i]
#         if digit_r[le_ - i]  < digit_r[le_ - i - 1]:
#             digit_r[le_ - i], digit_r[le_ - i - 1] = digit_r[le_ - i - 1], digit_r[le_ - i]
#         print(digit_r)
#
#
#
#     print()
# print(count_)
# print(digit_r)

from random import randint
def X3():

        l = [i*2 for i in range(11)]
        k = [i*2 for i in range(11,111)]


        ll = [max(l, key=lambda o:k[o])]
        w = (256 ** 6895665)

        time.sleep(2)

        return ll



def decorat(func):

    def inner():
        t0=time.time_ns()

        func()
        t1 = time.time_ns()
        print(round((t1-t0)/10**9,2))
        return func
    print(func.__name__)
    return inner


d = decorat(X3)
d()