def numerolog(N, c=1):

    if N< 10:
         return N
    return N%10 + numerolog(N//10)

Z=56
# c=1
# print(numerolog(Z))
# while numerolog(Z) > 9:
#     c=c+1
#
#     Z = numerolog(numerolog(Z))

# print(numerolog(Z),'count = ',c)

def cntr(f):
    cntr.i = 1
    def wrap(*args,**kwargs):
       print("A")
       res = f(*args, *kwargs)
       while  res > 9 :
           cntr.i += 1
           res = f(res)
       print(res)
       print(cntr.i)
       return
    return wrap

@cntr
numerolog()