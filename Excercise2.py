# The splat operator is especially useful when you want to receive an unknown number
# of arguments. Typically, you’ll expect that all of the arguments will be of the same
# type, although Python doesn’t enforce such a rule. In my experience, you’ll then take
# the tuple (numbers, in this case) and iterate over each element with either a for loop
# or a list comprehension

def mysum(args):
    total =0
    for i in [*args]:
        total=total+i
    return total

args=[1,7,5,7,4,3,]
print(mysum(args))
