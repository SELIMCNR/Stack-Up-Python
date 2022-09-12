letters = ["a", "b", "c", "d", "e"]

# use len() to count member of items in list
print(len(letters))

# use .append() to add new items into the list
letters.append("f")
print(letters)
letters.append("g")
print(letters)

# use .pop() to remove items from back of list
letters.pop()
print(letters)

# you can store items popped out of list
popped_item = letters.pop()
print(popped_item)

letters.pop(0)
print(letters)
