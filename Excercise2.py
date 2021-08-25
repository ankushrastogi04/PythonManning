# The splat operator is especially useful when you want to receive an unknown number
# of arguments. Typically, you’ll expect that all of the arguments will be of the same
# type, although Python doesn’t enforce such a rule. In my experience, you’ll then take
# the tuple (numbers, in this case) and iterate over each element with either a for loop
# or a list comprehension


def mysum(*args):
    total =0
    for i in [*args]:
        total=total+i
    return total

print(mysum(1,7,5,7,4,3))
print(mysum(1,7,4,3))
print(mysum(1,7,5,7,4))




#Beyond the excercise
def mysum(lst,n):
    total =0
    for i in lst:
        total=total+i
    return total+n

print(mysum([1,2,3], 4))

def mysum(lst):
    total =0
    cnt=0
    for i in lst:
        total=total+i
        cnt = cnt + 1
    return total/cnt

print(mysum([1,2,3]))
