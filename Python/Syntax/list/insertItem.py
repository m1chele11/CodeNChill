thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)


#add elements from another list

tropical = ["pineapple", "papaya", "mango"]
thislist.extend(tropical)

print(thislist)

thislist.remove("banana") #if more than one occurence this "remove" removes first occurence
print(thislist)

#pop removes the specified index, if not specified then it removes the last index
#clear empties the list
#del deletes the list