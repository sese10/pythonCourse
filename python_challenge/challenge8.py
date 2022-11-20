def evennumbers(values):
    only_even = [num for num in values if num % 2 == 0]
    print(only_even)


def evennumber(values):
    # iterating each number in list
    for num in values:
        # checking condition
        if num % 2 == 0:
            print(num, end=" ")


#  a. [1, 2, 3, 4, 5, 6]
# b. [ 34, 2, 9, 91, 19,401, 0 ]
evennumbers([1, 2, 3, 4, 5, 6] )
evennumber([1, 2, 3, 4, 5, 6] )

evennumbers([ 34, 2, 9, 91, 19,401, 0 ])
evennumber([ 34, 2, 9, 91, 19,401, 0 ])
