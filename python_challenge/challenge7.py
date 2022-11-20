def oddnumbers(values):
    only_odd = [num for num in values if num % 2 == 1]
    print(only_odd)


def oddnumber(values):
    # iterating each number in list
    for num in values:
        # checking condition
        if num % 2 != 0:
            print(num, end=" ")


# [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]
oddnumbers([1, 2, 3, 4, 5, 6])
oddnumber([1, 2, 3, 4, 5, 6])

oddnumbers([ 34, 2, 9, 91, 19,401, 0 ])
oddnumber([ 34, 2, 9, 91, 19,401, 0 ])
