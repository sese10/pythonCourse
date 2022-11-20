def removeduplicate(data):
    result = []
    if len(data) < 2:
        return data
    for i in data.casefold():
        if i not in result:
            result.append(i)
    print(''.join(result).capitalize())


def removeduplicatev2(data):
    data = data.casefold()
    result = [character for index, character in enumerate(data) if character not in data[:index]]
    print(''.join(result).capitalize())


# a. Hello: output shouldbe Helo b. Concatenate: output should be Conaten
removeduplicate('Hello')
removeduplicatev2('Hello')

removeduplicate('Concatenate')
removeduplicatev2('Concatenate')
