# declare a dictionary with any key-value pair of items/elements
# print the dictionary in console
# update the dictionary with two different key-value pair items
# print the dictionary in console again


animals = {
    "bird": "Parrot",
    "mammal": "Cow",
    "fish": "Titus"
}
print("dictionary:", animals)

# get -> fetch a value using specified key
bird = animals.get("bird")
print("get-1:", bird)
mammal = animals.get("mammal")
print("get-2:", mammal)

# item -> list of the dictionary key-value pair
animals_items = animals.items()
print("items:", animals_items)

#keys -> return the keys as a list
animals_values = animals.values()
print("values:", animals_values)

#keys -> return the keys as a list
animals_keys = animals.keys()
print("keys:", animals_keys)

# pop -> remove a key-value pair using the specified key
animals.pop("mammal")
print("pop:", animals)

# update -> add more key-value pairs into a dictionary
animals.update({"mammal": "Goat"})
animals.update({"insect": "Ant", "reptile": "Snake"})
print("update:", animals)

#popitem -> remove the last key-value pair from the dictionary
animals.popitem()
print("popitem:", animals)

#copy -> return a copy of a dictionary
copied_animals = animals.copy()
print("copy:", copied_animals)

# clear -> removes all the elements, items, key-value pair from the dictionary
animals.clear()
print("clear:", animals)
print("clear:", copied_animals)