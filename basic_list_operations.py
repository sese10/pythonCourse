# declare a list with any value and number of item/element
# print the list in console
# sort the list
# print the list in console again

myFamily = ["Bella", "Sandra", "Victoria", "Kate"]
print("List:", myFamily)

myFamily.sort()
print("sort.asc:", myFamily)
myFamily.sort(reverse=True)
print("sort.desc:", myFamily)








"""
languages = ["python", "java", "c#"]
print("List:", languages)

# append -> add new item at end of list
languages.append("javaScript")
print("append:", languages)

# insert -> add new item at any position in the list
languages.insert(0, "c")
languages.insert(2, "php")
print("insert:", languages)

# pop -> remove an item from the specified position (by index)
languages.pop(0)
print("pop:", languages)
languages.pop()
print("pop:", languages)

# remove -> remove an item by value
languages.remove("php")
print("remove:", languages)

# count -> return the number of occurrence in a list
languages.append("java")
count_java = languages.count("java")
print("list:", languages)
print("count:", count_java)

# len -> count the number of item in a list
length = len(languages)
print("len:", length)

# clear -> deletes all items in a list
languages.clear()
length = len(languages)
print("clear:", languages, length)

languages = ["python", "java", "c#"]

# copy -> return a copy of the list
languages_copy = languages.copy()
print("copy:", languages_copy)

# reverse -> reverse the order of items in the list
before_reverse = languages.copy()
languages.reverse()
print("before reverse:", before_reverse, "after reverse", languages)

languages = ["python", "java", "c#", "c", "smalltalk", "ruby"]

# sort -> sort the item in the list by either ascending or descending order
languages.sort()
print("sort.asc:", languages)
languages.sort(reverse=True)
print("sort.desc:", languages)

# extend -> add the content of the specified list to our current list
languages.extend(["visual basic", "brainfuck", "ring","sql", "powershell"])
print("extend:", languages)"""